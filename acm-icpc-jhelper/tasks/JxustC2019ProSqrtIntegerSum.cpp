#include "../library/header.hpp"
#include "../library/bigint.hpp"

class JxustC2019ProSqrtIntegerSum {
public:
	void solve(std::istream& in, std::ostream& out) {
	    uint64_t n;
	    in >> n;
        BigInt sqrt_n_1(sqrt(n));
        uint64_t sum_val = (sqrt_n_1 - 1) * sqrt_n_1 * (2 * sqrt_n_1 - 1) / 3 + sqrt_n_1 * (sqrt_n_1 - 1) / 2;
        sum_val -= sqrt_n_1 * sqrt_n_1 * sqrt_n_1;
        sum_val += (n + 1) * sqrt_n_1;
        out << sum_val << endl;
	}
};
