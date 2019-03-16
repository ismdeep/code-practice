//
// Created by ismdeep on 2019-03-16.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    int a = 10;
    int b = 100;
    printf("&a: %p\n", &a);
    printf("&b: %p\n", &b);

    size_t ap = (size_t) &a;
    size_t bp = (size_t) &b;

    printf("%lu\n", ap - bp);

    return 0;
}