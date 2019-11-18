#include "../library/header.hpp"

class JxustC2019ProACounterProblem {
public:
	void solve(std::istream& in, std::ostream& out) {
	    uint64_t n, p;
	    in >> n >> p;
	    uint64_t current = p;
	    uint64_t cnt = 0;
	    while (current <= n) {
	        cnt += (n / current);
	        current *= p;
	    }
	    out << cnt << endl;
	}
};
