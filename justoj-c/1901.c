//
// Created by ismdeep on 2019-02-27.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    bool arr[22][200];
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int n, a, b;
    arr[0][0] = arr[1][0] = 1;
    for(int i = 2; i < 21; ++i){
        arr[i][0] = 1; //0一定有，有则标记
        for(int j = 1; j < i; ++j){
            a = j; b = i - j;
            for(int k = 0; k <= (b-1) * b / 2; ++k)
                if(arr[b][k]) arr[i][a * b + k] = 1;
        }
    }
    while(scanf("%d", &n) == 1){
        for(int i = 0; i <= (n-1) * n / 2; ++i)
            if(i == 0) printf("%d", i);
            else if(arr[n][i]) printf(" %d", i);
        printf("\n");
    }
    return 0;
}
