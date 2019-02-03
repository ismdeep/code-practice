//
// Created by ismdeep on 2019-02-03.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>


bool is_leap_year(int y) {
    return y % 400 == 0 || (y % 4 == 0 && y % 100 != 0);
}


int main(int argc, char* argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int y, m, d;
    int cnt = 0;
    int month_days[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    scanf("%d-%d-%d", &y, &m, &d);
    if (is_leap_year(y)) month_days[2] = 29;
    for (int i = 1; i < m; ++i) {
        cnt += month_days[i];
    }
    cnt += d;
    printf("这个日期是这一年的第%d天\n", cnt);
    return 0;
}