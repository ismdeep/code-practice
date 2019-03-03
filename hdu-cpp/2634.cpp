//
// Created by ismdeep on 2019-03-03.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
using namespace std;

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int nn = n;
        double tmp;
        double sum = 0.00;
        while (nn--) {
            scanf("%lf", &tmp);
            sum += tmp;
        }
        printf("The average M = %.10llf.\n", sum / n);
    }
    return 0;
}
