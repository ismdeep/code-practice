//
// Created by ismdeep on 2019-03-17.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    size_t n;
    scanf("%lu", &n);
    double * a = (double *)malloc(sizeof(double) * n);
    for (size_t i = 0; i < n; i++) {
        scanf("%lf", &a[i]);
    }
    double avg = 0.00;
    double max_val = a[0];
    double min_val = a[0];
    for (size_t i = 0; i < n; ++i) {
        avg += a[i];
        if (a[i] > max_val) max_val = a[i];
        if (a[i] < min_val) min_val = a[i];
    }
    printf("%.3lf %.3lf %.3lf\n", avg / n, max_val, min_val);
    return 0;
}