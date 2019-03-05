def main():
    while True:
        try:
            s = input().strip()
            if '' == s:
                continue
            n = int(s)
            ans = 0
            tmp = 3
            while n >= tmp:
                ans += int(n / tmp)
                tmp *= 3
            print(ans)
        except:
            exit(0)


if __name__ == '__main__':
    main()
