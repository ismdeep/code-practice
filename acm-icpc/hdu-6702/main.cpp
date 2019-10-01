#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
#endif
    int t;
    scanf("%d", &t);
    while (t--) {
        unsigned int a, b;
        scanf("%u%u", &a, &b);
        unsigned int c = a & b;
        if (c == 0 && ((a^c)&(b^c)) == 0) {
            c = 1;
        }
        printf("%u\n", c);
    }
    return 0;
}