#include <iostream>
#include "../library/header.hpp"
#include "../library/computational_geometry.hpp"

class Aizu0010 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int n;
        in >> n;
        while (n--) {
            double x1, y1, x2, y2, x3, y3;
            in >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
            Point p1(x1, y1);
            Point p2(x2, y2);
            Point p3(x3, y3);
            Line la = ppline(p1, p2);
            Line lb = ppline(p2, p3);
            Point cross_point = lb.crosspoint(la);
            char ch[1024];
            sprintf(ch, "%.3lf %.3lf %.3lf", cross_point.x, cross_point.y, cross_point.distance(p1));
            out << ch << std::endl;
        }
    }
};
