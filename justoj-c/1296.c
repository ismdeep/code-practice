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
    int a;
    char b;
    double c;
    scanf("%d%c%lf", &a, &b, &c);
    printf("a=%d,b=%c,c=%lf\n", a, b, c);
    return 0;
}