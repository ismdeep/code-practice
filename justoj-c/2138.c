//
// Created by ismdeep on 2019-02-21.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int func(char *str,char ch) {
    int index = 0;
    int cnt = 0;
    while (str[index] != '\0') {
        if (ch == str[index]) {
            ++cnt;
        }
        ++index;
    }
    return cnt;
}

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    char str[1024];
    fgets(str, 1024, stdin);
    char ch;
    scanf("%c", &ch);
    printf("%d\n", func(str, ch));
    return 0;
}