#include "../library/header.hpp"


class Solution {
public:
    int m, n;
    int a[25][25];
    int ans;

    void dfs(int x, int y, int t) {
        int mx = -233333333, nx, ny;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (this->a[i][j] > mx) {
                    mx = a[i][j], nx = i, ny = j;
                }
            }
        }

        if (y == 0) {
            y = ny;
        }
        int nt = abs(nx - x) + abs(ny - y) + nx + 1;  //采摘最大值并返回路边的总时间
        if (t < nt || !this->a[nx][ny]) {
            return;
        }
        else { this->ans += a[nx][ny], a[nx][ny] = 0, dfs(nx, ny, t - nt + nx); }
    }
};


class JustOJ1502 {
public:
    void solve(std::istream &in, std::ostream &out) {
        Solution instance;
        int k;
        in >> instance.m >> instance.n >> k;
        for (int i = 1; i <= instance.m; i++) {
            for (int j = 1; j <= instance.n; j++) {
                in >> instance.a[i][j];
            }
        }
        instance.ans = 0;
        instance.dfs(0, 0, k);
        out << instance.ans << endl;
    }
};
