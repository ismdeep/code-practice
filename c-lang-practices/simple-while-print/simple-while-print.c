#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <unistd.h>

int main() {
    char msg[]= "hello man.";
    printf("%p\n", msg);
    while (true) {
        printf("%s\n", msg);
        sleep(1);
    }
    return 0;
}