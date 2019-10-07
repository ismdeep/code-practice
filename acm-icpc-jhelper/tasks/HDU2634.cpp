#include "../library/header.hpp"

class HDU2634 {
public:
	void solve(std::istream& in, std::ostream& out) {
        int t;
        in >> t;
        TIMES(tid, t) {
            int n;
            in >> n;
            int nn = n;
            double tmp;
            double sum = 0.00;
            while (nn--) {
                in >> tmp;
                sum += tmp;
            }
            char ch[1024];
            sprintf(ch, "The average M = %.10llf.", sum / n);
            string str = ch;
            out << str << endl;
        }
	}
};
