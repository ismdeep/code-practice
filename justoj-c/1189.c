//
// Created by ismdeep on 2019-02-03.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

size_t type_fun(char ch) {
    if ('A' <= ch && ch <= 'Z') return 0;
    if ('a' <= ch && ch <= 'z') return 1;
    if ('0' <= ch && ch <= '9') return 2;
    if (' ' == ch) return 3;
    if ('\n' == ch) return 5;
    return 4;
}

int main(int argc, char* argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    char buff[1024];
    uint64_t cnt[6];
    for (size_t i = 0; i < 6; ++i) cnt[i] = 0;
    fgets(buff, 1024, stdin);
    for (size_t i = 0; i < strlen(buff); ++i) {
        if (type_fun(buff[i]) == 0) ++cnt[0];
    }
    fgets(buff, 1024, stdin);
    for (size_t i = 0; i < strlen(buff); ++i) {
        if (type_fun(buff[i]) == 1) ++cnt[1];
    }
    fgets(buff, 1024, stdin);
    for (size_t i = 0; i < strlen(buff); ++i) {
        if (type_fun(buff[i]) == 2) ++cnt[2];
    }
    fgets(buff, 1024, stdin);
    for (size_t i = 0; i < strlen(buff); ++i) {
        if (type_fun(buff[i]) == 3) ++cnt[3];
    }
    fgets(buff, 1024, stdin);
    for (size_t i = 0; i < strlen(buff); ++i) {
        if (type_fun(buff[i]) == 4) ++cnt[4];
    }
    for (size_t i = 0; i < 5; ++i) {
        printf("%llu\n", cnt[i]);
    }
    return 0;
}