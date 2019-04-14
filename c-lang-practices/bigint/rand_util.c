//
// Created by ismdeep on 2019-04-14.
//

#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <sys/time.h>


int rand_int(int from, int to) {
    struct timeval tp;
    gettimeofday(&tp, NULL);
    srand(tp.tv_sec * 1000000 + tp.tv_usec);
    int length = to - from + 1;
    int val = rand() % length;
    return val + from;
}

char *rand_bigint_str(int sign, int digital_size) {

    if (digital_size <= 0) return "0";

    struct timeval tp;
    gettimeofday(&tp, NULL);
    srand(tp.tv_sec * 1000000 + tp.tv_usec);

    char *data = (char *) malloc(sizeof(char) * (digital_size + 3));
    memset(data, 0, sizeof(char) * (digital_size + 2));
    int start_digital_index = 0;
    if (1 == sign) {
        data[0] = '-';
        start_digital_index = 1;
    }
    if (2 == sign) {
        if (rand() % 2 == 1) {
            data[0] = '-';
            start_digital_index = 1;
        }
    }

    for (int i = start_digital_index; i < digital_size + start_digital_index; ++i) {
        data[i] = '0' + (rand() % 10);
    }

    return data;
}