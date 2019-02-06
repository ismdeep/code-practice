//
// Created by ismdeep on 2019-02-06.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char* argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int n, m;
    scanf("%d%d", &n, &m);
    int ** a = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n; ++i) {
        a[i] = (int *)malloc(sizeof(int) * m);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf("%d", &a[i][j]);
        }
    }
    bool found = false;
    int tmp;
    scanf("%d", &tmp);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (tmp == a[i][j]) {
                found = true;
                printf("%d\n", i * m + j);
            }
        }
    }
    if (!found) {
        printf("-1\n");
    }
    return 0;
}