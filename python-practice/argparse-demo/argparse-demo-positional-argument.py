import argparse


parser = argparse.ArgumentParser()
parser.add_argument("echo", help="Input what echo what.")
args = parser.parse_args()
print(args.echo)
