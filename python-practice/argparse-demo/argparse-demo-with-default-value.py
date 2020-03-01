import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', help='host', default='127.0.0.1')
args = parser.parse_args()
print('host is %s' % args.host)
