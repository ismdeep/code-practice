#include "../library/header.hpp"

class Aizu0016 {
public:
    void solve(std::istream &in, std::ostream &out) {
        std::string str;
        double x = 0.00;
        double y = 0.00;
        double now = 90;
        double PI = 3.141592653;
        while (in >> str) {
            double a, b;
            sscanf(str.data(), "%lf,%lf", &a, &b);
            if (a == b && b == 0) {
                break;
            }
            x += cos(now * PI / 180) * a;
            y += sin(now * PI / 180) * a;
            now -= b;
        }
        out << (int)x << std::endl << (int)y << std::endl;
    }
};
