//
// Created by ismdeep on 2019-01-31.
//

#ifndef ISMDEEP_UTIL_H
#define ISMDEEP_UTIL_H

#include <stdint.h>

void * create_1d_arr(size_t size, size_t sizeof_item) {
    void * arr = malloc(sizeof_item * size);
    return arr;
}

void ** create_2d_arr(size_t rows, size_t cols, size_t sizeof_item) {
    void ** arr = (void **)malloc(sizeof(size_t) * rows);
    for (size_t row_id = 0; row_id < rows; ++row_id) {
        arr[row_id] = malloc(sizeof_item * cols);
    }
    return arr;
}

#endif //ISMDEEP_UTIL_H
