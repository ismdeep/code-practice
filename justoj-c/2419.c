//
// Created by ismdeep on 2019-08-17.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX_SIZE 510

int dir[4][2] = {
        {0,  1},
        {1,  0},
        {0,  -1},
        {-1, 0}
};

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
#endif
    int a[MAX_SIZE][MAX_SIZE];
    bool visited[MAX_SIZE][MAX_SIZE];
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d%d", &n, &m);
        memset(a, 0, sizeof(a));
        memset(visited, 0xff, sizeof(visited));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                scanf("%d", &a[i][j]);
                visited[i][j] = false;
            }
        }
        /* start searching */
        int dir_index = 0;
        int x = 1;
        int y = 1;
        while (true) {
//            printf("x, y => %d %d\n", x, y);
            printf("%d ", a[x][y]);
            visited[x][y] = true;
            if (visited[x + dir[0][0]][y + dir[0][1]] && visited[x + dir[1][0]][y + dir[1][1]] && visited[x + dir[2][0]][y + dir[2][1]] && visited[x + dir[3][0]][y + dir[3][1]]) {
                break;
            }
            if (visited[x + dir[dir_index][0]][y + dir[dir_index][1]]) {
                dir_index = (dir_index + 1) % 4;
            }
            x = x + dir[dir_index][0];
            y = y + dir[dir_index][1];
        }
        printf("\n");
    }
    return 0;
}