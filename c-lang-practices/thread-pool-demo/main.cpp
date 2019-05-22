#include <iostream>
#include <unistd.h>
#include <thread>
#include <mutex>

using namespace std;

#define TIMES(id, n) for (int id = 0; id < (n); ++id)
#define TIMESRANGE(id, from, to) for (int id = (from); id <= (to); ++id)
#define TIMESREVERSE(id, fromlarge, tosmall) for (int id = (fromlarge); id >= (tosmall); --id)

#define THREAD_SIZE 4

int running_count = 0;
mutex _mutex_;


int fib(int n) {
    return n < 2 ? 1 : fib(n - 1) + fib(n - 2);
}


void thread_fun(int mm) {
//    printf("entering thread_fun(%d)\n", mm);
    printf("%d: fib(%d)\n", mm, fib(42));
//    printf("exiting thread_fun(%d)\n", mm);
    _mutex_.lock();
    --running_count;
    _mutex_.unlock();
}


int main() {
    thread t[100];
    for (int i = 0; i < 100;) {
        if (running_count < THREAD_SIZE) {
            t[i] = thread(thread_fun, i);
            _mutex_.lock();
            ++running_count;
            _mutex_.unlock();
            ++i;
        } else {
            usleep(10000);
        }
    }

    for (int i = 0; i < 100; ++i) {
        t[i].join();
    }
    return 0;
}