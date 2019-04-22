//
// Created by ismdeep on 2019-04-22.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int t;
    int tmp;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d%d", &n, &m);
        if (n % (m + 1) != 0) {
            printf("Ocean\n");
        } else {
            printf("Starry\n");
        }
        while (n--) {
            scanf("%d", &tmp);
        }
    }
    return 0;
}