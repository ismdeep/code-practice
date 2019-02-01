//
// Created by ismdeep on 2019-02-01.
//

#include <stdio.h>
#include <stdlib.h>
#include <ismdeep/time.h>


int main(int argc, char* argv[]) {
    printf("%llu us\n", get_current_timestamp_us());
    printf("%llu ms\n", get_current_timestamp_ms());
    printf("%llu s\n", get_current_timestamp_s());
    return 0;
}