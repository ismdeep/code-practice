//
// Created by ismdeep on 2019-03-22.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    unsigned char *a = (unsigned char *) malloc(sizeof(unsigned char) * 1024);
    size_t cnt = fread(a, sizeof(unsigned char), 1024, stdin);
    size_t ans = 0;
    for (size_t i = 0; i < cnt; ++i) {
        if ('\n' == a[i]) {
            break;
        }
        ++ans;
    }
    printf("%lu\n", ans);
    return 0;
}