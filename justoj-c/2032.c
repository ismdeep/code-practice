//
// Created by ismdeep on 2019-02-08.
//



#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

void try_swap(int a[], int i, int j) {
    if (a[i] > a[j]) {
        int tmp;
        tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}

int main(int argc, char *argv[]) {
    int a[10];
    int top = -1;
    int tmp;
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int n;
    while (scanf("%d", &n) != EOF) {
        top = -1;
        while (n--) {
            scanf("%d", &tmp);
            if (top < 3) {
                bool found = false;
                for (int i = 0; i <= top; ++i) {
                    if (a[i] == tmp) {
                        found = true;
                    }
                }
                if (!found) {
                    ++top;
                    a[top] = tmp;
                }
            }
        }

        if (top >= 3) {
            printf("ecjtujxnu\n");
        }else if (top <= 1){
            printf("jxust\n");
        }else{
            try_swap(a, 0, 1);
            try_swap(a, 1, 2);
            try_swap(a, 0, 1);
            if (a[1] - a[0] == a[2] - a[1]) {
                printf("jxust\n");
            }else{
                printf("ecjtujxnu\n");
            }
        }
    }
    return 0;
}