//
// Created by ismdeep on 2019-04-06.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[], char *envp[]) {
    printf("### ARGC ###\n%d\n", argc);
    printf("### ARGV ###\n");
    while (*argv)
        printf("%s\n", *(argv)++);
    printf("### ENVP ###\n");
    while (*envp)
        printf("%s\n", *(envp)++);
    return 0;
}