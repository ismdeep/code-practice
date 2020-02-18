#include "../library/header.hpp"
#include "../library/pow_mod.hpp"

class JustOJ1444 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    size_t n;
	    in >> n;
	    out << pow_mod(5438, n, 10) % 10 << endl;
	}
};
