//
// Created by ismdeep on 2019-02-06.
//



#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

void perm(int a[], int index, int n) {
    if (index >= n) {
        // output
        for (int i = 0; i < n; ++i) {
            printf("%4d", a[i]);
        }
        printf("\n");
    }

    for (int i = 1; i <= n; ++i) {
        bool found = false;
        for (int j = 0; j < index; ++j) {
            if (a[j] == i) {
                found = true;
            }
        }
        if (!found) {
            a[index] = i;
            perm(a, index + 1, n);
        }
    }

}

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int n;
    scanf("%d", &n);
    int a[10];
    perm(a, 0, n);
    return 0;
}