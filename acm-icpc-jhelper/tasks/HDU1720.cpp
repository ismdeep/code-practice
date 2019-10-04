#include "../library/header.hpp"

class HDU1720 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string str_a, str_b;
	    int a, b;
	    while (in >> str_a >> str_b) {
	        sscanf(str_a.data(), "%x", &a);
	        sscanf(str_b.data(), "%x", &b);
	        out << a + b << endl;
	    }
	}
};
