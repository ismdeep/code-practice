#include "../library/header.hpp"

bool is_ok(int val) {
    if (val < 100) {
        return false;
    }
    if (val > 999) {
        return false;
    }
    int a, b, c, t;
    t = val;
    c = t % 10; t /= 10;
    b = t % 10; t /= 10;
    a = t % 10;
    return val == a*a*a + b*b*b + c*c*c;
}

class DOTCPP1016 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    FOR(int, val, 100, 999, 1) {
	        if (is_ok(val)) {
	            out << val << endl;
	        }
	    }
	}
};
