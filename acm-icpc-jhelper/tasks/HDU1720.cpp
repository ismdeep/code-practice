#include "../library/header.hpp"

class HDU1720 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string stra, strb;
	    int a, b;
	    while (in >> stra >> strb) {
	        sscanf(stra.data(), "%x", &a);
	        sscanf(strb.data(), "%x", &b);
	        out << a + b << endl;
	    }
	}
};
