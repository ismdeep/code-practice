//
// Created by ismdeep on 2019-01-31.
//

#include <stdio.h>
#include <stdlib.h>
#include <ismdeep/util.h>


int main(int argc, char * argv[]) {

    uint64_t * arr1 = create_1d_arr(10, sizeof(uint64_t));
    uint64_t ** arr2 = create_2d_arr(10, 20, sizeof(uint64_t));

    return 0;
}