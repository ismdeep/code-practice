#include <iostream>
#include <unistd.h>
#include <thread>

using namespace std;

#define TIMES(id, n) for (int id = 0; id < (n); ++id)
#define TIMESRANGE(id, from, to) for (int id = (from); id <= (to); ++id)
#define TIMESREVERSE(id, fromlarge, tosmall) for (int id = (fromlarge); id >= (tosmall); --id)
#define THREAD_SIZE 2


int pool[THREAD_SIZE];

int fib(int n) {
    return n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
}


void thread_fun(int mm) {
    printf("thread_fun(%d)\n", mm);
    while (true) {
        if (-1 != pool[mm]) {
            printf("%d => %d\n", mm, fib(40));
            pool[mm] = -1;
        }
        sleep(1);
    }

}


void worker() {
    int mm = 0;
    while (mm < 256) {
        TIMES(workderid, THREAD_SIZE) {
            if (-1 == pool[workderid] && mm < 256) {
                pool[workderid] = mm;
                ++mm;
            }
        }
        sleep(1);
    }
}


int main() {
    TIMES(i, THREAD_SIZE) {
        pool[i] = -1;
    }

    thread t[THREAD_SIZE];
    TIMES(threadid, THREAD_SIZE) {
        t[threadid] = thread(thread_fun, threadid);
    }

    TIMES(threadid, THREAD_SIZE) {
        t[threadid].join();
    }

    return 0;
}