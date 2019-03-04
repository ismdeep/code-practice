//
// Created by ismdeep on 2019-03-04.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <ismdeep/time.h>

#define MAXN 100000000

int main(int argc, char *argv[]) {
    struct timeval start_time;
    uint64_t *a = (uint64_t *) malloc(MAXN * sizeof(uint64_t));
    create_start_point(&start_time);
    memset(a, 0, MAXN * sizeof(uint64_t));
    printf("%llums\n", stop_watch_ms(start_time));

    create_start_point(&start_time);
    for (size_t i = 0; i < MAXN; ++i) {
        a[i] = 0;
    }
    printf("%llums\n", stop_watch_ms(start_time));


    return 0;
}