//
// Created by ismdeep on 2019-04-06.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    printf("The current process ID is: %d\n", getpid());
    return 0;
}