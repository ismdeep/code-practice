#include "../library/header.hpp"

class HDU2268 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int a, b, c;
	    while (in >> a >> b >> c) {
            double t;
            double s1;
            if (b > a) {
                s1 = ((b + a) * 1.0 / (b + 3 * a)) * c;
                t = s1 / b + (c - s1) / a;
            } else {
                t = c * 1.0 / a;
            }
            char ch[1024];
            sprintf(ch, "%.3f", t);
            string str = ch;
            out << str << endl;
	    }
	}
};
