def main():
    while True:
        try:
            s = input().strip()
            if '' == s:
                continue
            n = int(s)
            print('1' if n is 0 else '6')
        except:
            exit(0)


if __name__ == '__main__':
    main()
