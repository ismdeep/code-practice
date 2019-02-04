//
// Created by ismdeep on 2019-02-04.
//
#ifndef _ISMDEEP_ARGV_H
#define _ISMDEEP_ARGV_H

#include <string.h>
#include <stdint.h>
#include <stdbool.h>

char * get_argv(int argc, char * argv[], const char * search_key) {
    for (size_t i = 0; i < argc - 1; ++i) {
        if (strcmp(search_key, argv[i]) == 0) {
            return argv[i+1];
        }
    }
    return "";
}


bool argv_exist_switch(int argc, char* argv[], const char * search_key) {
    for (size_t i = 0; i < argc; ++i) {
        if (strcmp(argv[i], search_key) == 0) {
            return true;
        }
    }
    return false;
}
#endif