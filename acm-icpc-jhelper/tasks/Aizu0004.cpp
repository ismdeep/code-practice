#include "../library/header.hpp"

class Aizu0004 {
public:
    void solve(std::istream &in, std::ostream &out) {
        double a, b, c, d, e, f;
        while (in >> a >> b >> c >> d >> e >> f) {
            double x = (c * e - b * f) / (a * e - b * d);
            double y = (a * f - c * d) / (a * e - b * d);
            if (x == 0) x = 0.00;
            if (y == 0) y = 0.00;
            char ch[1024];
            sprintf(ch, "%.3lf %.3lf", x, y);
            string ans = ch;
            out << ans << endl;
        }
    }
};
