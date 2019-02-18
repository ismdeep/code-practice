//
// Created by ismdeep on 2019-02-18.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    double r, h;
    scanf("%lf %lf", &r, &h);
    double v = 3.14159 * r * r * h / 3.0;
    printf("V=%lf\n", v);
    return 0;
}