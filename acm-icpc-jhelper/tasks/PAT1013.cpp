#include "../library/header.hpp"
#include "../library/prime.hpp"

class PAT1013 {
public:
	void solve(std::istream& in, std::ostream& out) {
        PrimeTable prime_table = PrimeTable::generate(200000);

	    size_t m, n;
        in >> m >> n;
        bool flag = false;

        FOR(size_t, prime_id, 0, n - m, 1) {
            if (flag) {
                out << " ";
            }
            flag = true;
            out << prime_table.data[prime_id + m - 1];
            if ((prime_id + 1) % 10 == 0) {
                out << endl;
                flag = false;
            }
        }
        if (flag) {
            out << endl;
        }
	}
};
