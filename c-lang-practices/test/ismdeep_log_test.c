//
// Created by ismdeep on 2019-01-31.
//

#include <stdio.h>
#include <stdlib.h>
#include <ismdeep/log.h>

int main(int argc, char * argv[]) {
    log_with_stdout = true;
    write_log(LOG_INFO, "write %d", 1);
    return 0;
}