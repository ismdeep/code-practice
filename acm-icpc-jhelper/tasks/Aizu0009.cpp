#include "../library/header.hpp"
#include "../library/prime.hpp"

class Aizu0009 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    bool* is_prime = generate_is_prime_table(999999);
	    uint64_t n;
	    while (in >> n) {
	        uint64_t cnt = 0;
	        FOR(uint64_t, i, 2, n+1, 1) {
	            if (is_prime[i]) {
	                ++cnt;
	            }
	        }
	        out << cnt << std::endl;
	    }
	}
};
