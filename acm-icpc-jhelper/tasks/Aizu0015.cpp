#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include "../library/bigint.hpp"

class Aizu0015 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int t;
	    in >> t;
	    while (t--) {
            std::string a, b;
            in >> a >> b;
            BigInt bigint_a(a);
            BigInt bigint_b(b);
            BigInt sum = bigint_a + bigint_b;
            if (sum.to_string().length() > 80) {
                out << "overflow" << std::endl;
            } else {
                out << sum.to_string() << std::endl;
            }

	    }

	}
};
