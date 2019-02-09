//
// Created by ismdeep on 2019-02-09.
//
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define ll long long int

ll n,m;

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    while(scanf("%lld%lld", &n, &m) != EOF){
        ll ans = (m - n + 1)%15;
        ll sum = 0;
        while(ans--){
            sum += n%15;
            n++;
        }
        sum %= 15;
        printf("%lld\n", sum);
    }
    return 0;
}
