//
// Created by ismdeep on 2019-02-01.
//

#ifndef ISMDEEP_TIME_H
#define ISMDEEP_TIME_H

#include <sys/time.h>
#include <stdint.h>

uint64_t get_current_timestamp_s() {
    struct timeval t;
    gettimeofday(&t, NULL);
    return t.tv_sec;
}

uint64_t get_current_timestamp_ms() {
    struct timeval t;
    gettimeofday(&t, NULL);
    uint64_t timestamp = (uint64_t)t.tv_sec * 1000 + t.tv_usec / 1000;
    return timestamp;
}


uint64_t get_current_timestamp_us() {
    struct timeval t;
    gettimeofday(&t, NULL);
    uint64_t timestamp = (uint64_t)t.tv_sec * 1000000 + t.tv_usec;
    return timestamp;
}

#endif //ISMDEEP_TIME_H
