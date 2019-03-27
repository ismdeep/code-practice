//
// Created by ismdeep on 2019-03-27.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <string.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int n, m;
    while (cin >> n >> m) {
        int vv[61], pp[61], qq[61];
        memset(vv, 0, sizeof(vv));
        memset(pp, 0, sizeof(pp));
        memset(qq, 0, sizeof(qq));


        int p[61][4], v[61][4];
        int a[61][2];         //一个主件最多有两个附件，没有的话就记为0
        memset(v, 0, sizeof(v));
        memset(p, 0, sizeof(p));
        memset(a, 0, sizeof(a));

        for (int i = 1; i <= m; i++) {
            cin >> vv[i] >> pp[i] >> qq[i];
            if (qq[i])             //标记附件
            {
                if (!a[qq[i]][0])
                    a[qq[i]][0] = i;
                else
                    a[qq[i]][1] = i;
            }
        }
        int f[61][4];     //存放每种情况的价值v*p；
        memset(f, 0, sizeof(0));
        for (int i = 1; i <= m; i++)     //变成分组背包
        {
            if (!qq[i]) {
                f[i][0] = vv[i] * pp[i];
                f[i][1] = vv[a[i][0]] * pp[a[i][0]] + vv[i] * pp[i];
                f[i][2] = vv[a[i][1]] * pp[a[i][1]] + vv[i] * pp[i];
                f[i][3] = vv[a[i][0]] * pp[a[i][0]] + vv[a[i][1]] * pp[a[i][1]] + vv[i] * pp[i];

                v[i][0] = vv[i];
                v[i][1] = vv[a[i][0]] + vv[i];
                v[i][2] = vv[a[i][1]] + vv[i];
                v[i][3] = vv[a[i][0]] + vv[a[i][1]] + vv[i];
            }
        }


        int dp[n + 1];
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= m; i++)       //分组背包
        {
            if (!qq[i])
                for (int j = n; j >= 0; j--)
                    for (int k = 0; k < 4; k++) {
                        if (j - v[i][k] >= 0)
                            dp[j] = max(dp[j], dp[j - v[i][k]] + f[i][k]);
                    }
        }
        cout << dp[n] << endl;
    }
    return 0;
}