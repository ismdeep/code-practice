//
// Created by ismdeep on 2019-07-12.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

#define MAXN 200000


int max(int a, int b) {
    return a > b ? a : b;
}


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
    int x2 = 0;
    int x3 = 0;
    int x4 = 0;
    int x5 = 0;
    for (int x1 = 0; x1 < n; x1++) {
        if ('x' == a[x1]) {
            bool x2_found = false;
            x2 = max(x1 + 1, x2);
            while (x2 < n) { if ('t' == a[x2]) { x2_found = true; break; } ++x2; }
            if (!x2_found) {break;}

            bool x3_found = false;
            x3 = max(x2 + 1, x3);
            while (x3 < n) { if ('C' == a[x3]) { x3_found = true; break; } ++x3; }
            if (!x3_found) {break;}

            bool x4_found = false;
            x4 = max(x3 + 1, x4);
            while (x4 < n) { if ('p' == a[x4]) { x4_found = true; break; } ++x4; }
            if (!x4_found) {break;}

            bool x5_found = false;
            x5 = max(x4 + 1, x5);
            while (x5 < n) { if ('c' == a[x5]) { x5_found = true; break; } ++x5; }
            if (!x5_found) {break;}
            ++x2;
            ++x3;
            ++x4;
            ++x5;
            ++cnt;
        }
    }
    printf("%d\n", cnt);
    return 0;
}