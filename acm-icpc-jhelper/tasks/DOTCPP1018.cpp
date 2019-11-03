#include "../library/header.hpp"

class DOTCPP1018 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n, t;
	    double sum = 0.00;
	    in >> n;
	    int a, b;
	    a = 2;
	    b = 1;
	    TIMES(i, n) {
	        sum += (double)a / b;
	        t = a;
	        a = a + b;
	        b = t;
	    }
	    char ans[1024];
	    sprintf(ans, "%.2f", sum);
	    string ans_str = ans;
	    out << ans_str << endl;
	}
};
