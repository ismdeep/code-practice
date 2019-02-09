//
// Created by ismdeep on 2019-02-09.
//
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>

struct Point {
    double x, y;
};

double distance(struct Point a, struct Point b) {
    return sqrt((a.x - b.x)  * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double triangle_area(struct Point p1, struct Point p2, struct Point p3) {
    double a, b, c;
    a = distance(p1, p2);
    b = distance(p1, p3);
    c = distance(p2, p3);
    double s = (a + b + c) / 2.0;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

double min(double a, double b) {
    return a < b ? a : b;
}

int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
    freopen("../in.txt", "r", stdin);
#endif
    int val1, val2;
    struct Point p1, p2, p3, p4;
    scanf("%d%d", &val1, &val2);
    p1.x = val1; p1.y = val2;
    scanf("%d%d", &val1, &val2);
    p2.x = val1; p2.y = val2;
    scanf("%d%d", &val1, &val2);
    p3.x = val1; p3.y = val2;
    scanf("%d%d", &val1, &val2);
    p4.x = val1; p4.y = val2;

    double area1 = triangle_area(p1, p2, p3) + triangle_area(p1, p3, p4);
    double area2 = triangle_area(p1, p2, p4) + triangle_area(p2, p3, p4);

    printf("%.3lf\n", min(area1, area2));

    return 0;
}