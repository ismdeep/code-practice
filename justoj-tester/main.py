import os
import sys


def get_file_list(__dir__):
    file_list = []
    for home, dirs, files in os.walk(__dir__):
        for filename in files:
            if filename[len(filename) - 3:] == '.in':
                file_list.append(filename[:len(filename) - 3])
    return file_list


def main():
    if len(sys.argv) < 3:
        print('Usage: python3 main.py <data-path> <program-cmd>')
        exit(0)
    data_path = sys.argv[1]
    cmd = sys.argv[2]
    file_list = get_file_list(data_path)
    for filename in file_list:
        inpath = os.path.join(data_path, filename + ".in")
        outpath = os.path.join(data_path, filename + ".out")
        os.system("{} < {} > tmp.out".format(cmd, inpath))
        os.system("diff tmp.out {}".format(outpath))
        print("{} Done.".format(filename))
        print('-' * 40)


if __name__ == '__main__':
    main()
