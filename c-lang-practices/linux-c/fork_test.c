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
    int count = 0;
    pid_t pid;
    pid = fork();
    if (pid < 0) {
        printf("error in fork!\n");
        exit(1); /* fork 出错退出 */
    } else if (pid == 0) {
        printf("I am the child process, the count is %d, my process ID is %d\n", count, getpid());
    } else {
        printf("I am the parent process, the count is %d, my process ID is %d\n", ++count, getpid());
    }
    return 0;
}