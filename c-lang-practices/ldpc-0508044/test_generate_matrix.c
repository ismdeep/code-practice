//
// Created by ismdeep on 2019-04-20.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <generate_matrix.h>

int main(int argc, char *argv[]) {
    uint8_t **a = generate_A(8, 2, 4);
    print_matrix(a, 8);
    return 0;
}