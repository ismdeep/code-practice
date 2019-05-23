#include <iostream>
#include <unistd.h>
#include <thread>
#include <mutex>

using namespace std;

#define THREAD_SIZE 4

int running_count = 0;
mutex _mutex_;


int fib(int n) {
    return n < 2 ? 1 : fib(n - 1) + fib(n - 2);
}


void thread_fun(int mm) {
    printf("%d: fib(%d)\n", mm, fib(42));
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