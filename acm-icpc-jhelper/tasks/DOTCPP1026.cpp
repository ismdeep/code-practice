#include "../library/header.hpp"

class DOTCPP1026 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int a[10];
	    TIMES(i, 10) {
	        in >> a[i];
	    }
	    TIMES(i,10) {
	        out << a[9 - i] << " ";
	    }
	    out << endl;
	}
};
