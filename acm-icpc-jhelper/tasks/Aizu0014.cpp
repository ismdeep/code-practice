#include "../library/header.hpp"

class Aizu0014 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int a;
	    while (in >> a) {
	        int b = 0;
	        TIMES(i,600 / a) {
	            b += a*i*a*i*a;
	        }
	        out << b << endl;
	    }
	}
};
