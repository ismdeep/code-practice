//
// Created by ismdeep on 2019-03-17.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    uint64_t *val;
    val = 0x7ffeec0077d8;
    printf("%llu\n", *val);
    *val = 1;
    return 0;
}