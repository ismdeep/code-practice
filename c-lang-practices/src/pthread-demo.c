//
// Created by ismdeep on 2019-02-17.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <pthread.h>

// Let us create a global variable which will be changed in threads
int g = 0;
int count_down = 0;
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;

// The function to be executed by all threads
void *myThreadFun(void *vargp) {
    // Store the value argument passed to this thread
    int *myid = (int *)vargp;
    int i;
    // Let us create a static variable to observe its changes
    static int s = 0;
    // Change static and global variables

    for (int i = 0; i < 1000; i++) {
        pthread_mutex_lock(&mutex1);
        ++g;
        pthread_mutex_unlock(&mutex1);
    }
    printf("Thread ID: %p, Global: %d\n", myid, g);
}


int main(int argc, char *argv[]) {
    int i;
    g = 0;
    count_down = 1000;
    pthread_t ret[1000];
    for (i = 0; i < 1000; ++i) {
        pthread_create(&ret[i], NULL, myThreadFun, (void *)&ret[i]);
    }
    for (i = 0; i < 1000; ++i) {
        pthread_join(ret[i], NULL);
    }
    printf("%d\n", g);
    return 0;
}