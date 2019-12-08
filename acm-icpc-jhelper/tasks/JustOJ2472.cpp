#include "../library/header.hpp"
#include "../library/bigint.hpp"

class JustOJ2472 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string str;
	    in >> str;
	    BigInt n = str;
        BigInt sqrt_n_1 = sqrt(n);
        BigInt sum_val =
                (sqrt_n_1 - 1) * sqrt_n_1 * (2 * sqrt_n_1 - 1) / 3
                + sqrt_n_1 * (sqrt_n_1 - 1) / 2
                + (n + 1) * sqrt_n_1
                - sqrt_n_1 * sqrt_n_1 * sqrt_n_1;
        out << sum_val << endl;
	}
};
