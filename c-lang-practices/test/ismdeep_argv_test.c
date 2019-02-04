//
// Created by ismdeep on 2019-02-04.
//

#include <stdio.h>
#include <stdlib.h>
#include <ismdeep/argv.h>

int main(int argc, char* argv[]) {
    printf("-sim flag: {%d}\n", argv_exist_switch(argc, argv, "-sim"));
    printf("-n = {%d}\n", atoi(get_argv(argc, argv, "-n")));
    return 0;
}