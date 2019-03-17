//
// Created by ismdeep on 2019-03-17.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <time.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    uint64_t val = 0;
    printf("%p\n", &val);
    printf("%llu\n", &val);
    while (true) {
        printf("%llu\n", val);
        usleep(1000 * 300);
    }
    return 0;
}