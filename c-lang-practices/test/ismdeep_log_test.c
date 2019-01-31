//
// Created by ismdeep on 2019-01-31.
//

#include <stdio.h>
#include <stdlib.h>
#include <ismdeep/log.h>

int main(int argc, char * argv[]) {
    write_log("/data/ismdeep.log", LOG_LEVEL_INFO, "log-test", "write %d", 1);
    return 0;
}