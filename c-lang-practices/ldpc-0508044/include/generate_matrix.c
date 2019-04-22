//
// Created by ismdeep on 2019-04-20.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <utils.h>

uint8_t ** generate_A (size_t n, size_t wc, size_t wr) {
    uint8_t **a = (uint8_t **) malloc(sizeof(uint8_t *) * n);
    TIMES(size_t , i, n) {
        a[i] = (uint8_t *) malloc(sizeof(uint8_t) * n);
        TIMES(size_t, j, n) {
            a[i][j] = j;
        }
    }
    return a;
}

void print_matrix(uint8_t **a, size_t n) {
    TIMES(size_t, i, n) {
        TIMES(size_t, j, n) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}