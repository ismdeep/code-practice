from gevent import monkey
monkey.patch_all()  # noqa

import logging

from dnslib import DNSRecord, QTYPE, DNSHeader, RR, A, MX, TXT, CNAME, RCODE
from gevent.server import DatagramServer
import requests
from requests.exceptions import ConnectionError

import logging


def setup_logging(loglevel_name):
    logging.basicConfig(
        level=getattr(logging, loglevel_name),
        format='[%(asctime)s][%(levelname)s]%(message)s',
    )


logger = logging.getLogger('dnsproxy')


class DNSProxy(DatagramServer):

    def __init__(self, listener, resolver_addr, handle=None,
                 spawn='default'):
        super().__init__(listener, handle, spawn)
        self.session = requests.Session()
        self.resolver_addr = resolver_addr.rstrip('/')

    def handle(self, data, address):
        request = DNSRecord.parse(data)
        req_id = request.header.id
        query_name = request.q.qname
        query_type = request.q.qtype

        logger.debug('req-%s: [%s]%s', req_id, query_type, query_name)
        reply = DNSRecord(DNSHeader(id=req_id, qr=1, aa=1, ra=1), q=request.q)

        try:
            resp = self.session.get(
                self.resolver_addr + '/{}'.format(query_name).rstrip('.'))
        except ConnectionError as e:
            logger.error('connection error to %s: %s', self.resolver_addr, e)
            reply.header.rcode = RCODE.SERVFAIL
        else:
            if resp.status_code == 200:
                ip = resp.text
                logger.debug('resp-%s: %s', req_id, ip)
                if query_type == QTYPE.A:
                    reply.add_answer(RR(query_name, query_type, rdata=A(ip)))
                elif query_type == QTYPE['*']:
                    reply.add_answer(RR(query_name, QTYPE.A, rdata=A(ip)))
                    reply.add_answer(RR(query_name, QTYPE.MX, rdata=MX(ip)))
                    reply.add_answer(RR(query_name, QTYPE.TXT, rdata=TXT(TXT)))
                else:
                    reply.add_answer(
                        RR(query_name, QTYPE.CNAME, rdata=CNAME(TXT)))
            elif resp.status_code == 404:
                logger.debug('resp-%s: %s', req_id, 'nxdomain')
                reply.header.rcode = RCODE.NXDOMAIN
            else:
                logger.debug('resp-%s: %s', req_id, 'unknown error')
                reply.header.rcode = RCODE.SERVFAIL
                logger.error(
                    'unexpected response from server: [%d]%s',
                    resp.status_code, resp.text
                )
        self.sendto(reply.pack(), address)


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        '-b', '--bind', default=':53',
        help='bind address. The default is ":53", '
             'which requires root privilege')
    parser.add_argument('server', help='address of the dnsproxy server')
    parser.add_argument('-l', '--loglevel', default='INFO',
                        choices=('DEBUG', 'INFO', 'WARNING', 'ERROR'))
    parser.add_argument('-p', '--protocol', default='http',
                        choices=('http', 'https'))
    args = parser.parse_args()
    setup_logging(args.loglevel)
    DNSProxy(
        args.bind, '{}://{}'.format(args.protocol, args.server)
    ).serve_forever()


if __name__ == '__main__':
    main()
