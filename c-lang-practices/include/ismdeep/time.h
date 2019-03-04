//
// Created by ismdeep on 2019-02-01.
//

#ifndef ISMDEEP_TIME_H
#define ISMDEEP_TIME_H

#include <sys/time.h>
#include <stdint.h>

void create_start_point(struct timeval * t) {
    gettimeofday(t, NULL);
}

uint64_t stop_watch_us(struct timeval t1) {
    struct timeval t2;
    gettimeofday(&t2, NULL);
    uint64_t timestamp1 = (uint64_t)t1.tv_sec * 1000000 + t1.tv_usec;
    uint64_t timestamp2 = (uint64_t)t2.tv_sec * 1000000 + t2.tv_usec;
    return timestamp2 - timestamp1;
}

uint64_t stop_watch_ms(struct timeval t1) {
    return stop_watch_us(t1) / 1000;
}

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
