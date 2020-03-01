import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', help='host')
args = parser.parse_args()
print('host is %s' % args.host)
