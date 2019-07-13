//
// Created by ismdeep on 2019-07-12.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

#define MAXN 200000

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int n;
    scanf("%d", &n);
    char* a = (char *) malloc(sizeof(char) * (n + 1));
    memset(a, 0, sizeof(char) * (n+1));
    scanf("%s", a);
    int cnt = 0;
    for (int x1 = 0; x1 < n; x1++) {

    }
    return 0;
}