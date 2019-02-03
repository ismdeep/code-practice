//
// Created by ismdeep on 2019-02-03.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char* argv[]) {
    int n;
    scanf("%d", &n);
    uint64_t ** a = (uint64_t **) malloc(sizeof(uint64_t *) * n);
    for (int i = 0; i < n; ++i) {
        a[i] = (uint64_t *) malloc(sizeof(uint64_t) * n);
    }
    for (int i = 0; i < n; ++i) {
        a[i][0] = 1;
        a[i][i] = 1;
    }
    for (int i = 2; i < n; ++i) {
        for (int j = 1; j < i; ++j) {
            a[i][j] = a[i-1][j-1] + a[i-1][j];
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            printf("%4d", a[i][j]);
        }
        printf("\n");
    }


    return 0;
}