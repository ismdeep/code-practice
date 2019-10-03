#include "../library/header.hpp"
#include "../library/computational_geometry.hpp"

class Aizu0012 {
public:
    void solve(std::istream &in, std::ostream &out) {
        double x1, y1, x2, y2, x3, y3, xp, yp;
        while (in >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> xp >> yp) {
            Point p1(x1, y1);
            Point p2(x2, y2);
            Point p3(x3, y3);
            Point pp(xp, yp);

            Triangle t123(p1, p2, p3);

            if (t123.point_in(pp)) {
                out << "YES" << endl;
            } else {
                out << "NO" << endl;
            }
        }
    }
};
