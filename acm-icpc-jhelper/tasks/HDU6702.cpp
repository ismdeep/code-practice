#include "../library/header.hpp"

class HDU6702 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int t;
	    in >> t;
	    TIMES(tid, t) {
            unsigned int a, b;
            in >> a >> b;
            unsigned int c = a & b;
            if (c == 0 && ((a^c)&(b^c)) == 0) {
                c = 1;
            }
            out << c << endl;
	    }
	}
};
