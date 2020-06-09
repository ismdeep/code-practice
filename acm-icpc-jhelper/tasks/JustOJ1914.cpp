#include "../library/header.hpp"

class JustOJ1914 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n;
	    while (in >> n, n) {
	        out << ceil(log(n) / log(3)) << endl;
	    }
	}
};
