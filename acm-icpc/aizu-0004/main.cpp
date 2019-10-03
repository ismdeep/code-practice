#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
#ifdef ISMDEEP_LOCAL
    freopen("../in.txt", "r", stdin);
#endif
    double a, b, c, d, e, f;
    while (scanf("%lf %lf %lf %lf %lf %lf", &a, &b, &c, &d, &e, &f) != EOF) {
        double x = (c * e - b * f) / (a * e - b * d);
        double y = (a * f - c * d) / (a * e - b * d);
        if (x == 0) x = 0.00;
        if (y == 0) y = 0.00;
        printf("%.3lf %.3lf\n", x, y);
    }
    return 0;
}