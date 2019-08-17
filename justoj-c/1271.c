#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

#define MAXN 100005
int cnt[MAXN], n;

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
#endif
    int t, ans;
    scanf("%d", &t);
    for (int k = 1; k <= t; k++) {
        ans = 1;
        int x, j = 0;
        scanf("%d", &n);
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++) {
            scanf("%d", &x);
            for (int j = 1; j * j <= x; j++) {
                if (x % j == 0) {
                    cnt[j]++;
                    if (x / j != j)
                        cnt[x / j]++;
                }

            }

        }
        for (int i = 100000; i >= 1; i--) {
            if (cnt[i] >= 2) {
                ans = i;
                break;
            }
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}