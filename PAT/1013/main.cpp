#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int* gen_primes() {
    const int max_n = 110000;
    int* a = (int*) malloc(max_n * sizeof(int));
    bool* is_prime = (bool*) malloc(max_n * sizeof(bool));
    for (int i = 0; i < max_n; ++i) {
        is_prime[i] = true;
    }
    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i * i <= max_n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= max_n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    uint64_t cnt = 0;
    for (int i = 0; i < max_n; i++) {
        if (is_prime[i]) {
            ++cnt;
            a[cnt] = i;
        }
    }
    return a;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int* prime = gen_primes();
    int cnt = 0;
    int start, end;
    cin >> start >> end;
    for (int i = start; i <= end; i++) {
        cout << prime[i];
        ++cnt;
        if (cnt == 10) {
            cout << endl;
        } else {
            if (i != end) {
                cout << " ";
            }
        }
        cnt %= 10;
    }
    if (cnt != 0) {
        cout << endl;
    }
    return 0;
}