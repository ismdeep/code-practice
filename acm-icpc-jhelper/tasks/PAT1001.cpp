#include "../library/header.hpp"


int count_step (int n) {
    if (1 == n) {
        return 0;
    }
    if (n % 2 == 0) {
        return 1 + count_step(n / 2);
    }
    return 1 + count_step((3 * n + 1) / 2);
}


class PAT1001 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n;
	    in >> n;
	    out << count_step(n) << endl;
	}
};
