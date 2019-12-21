#include "../library/header.hpp"

class JustOJ1000MemTest {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int size = 128 * 1024 * 1024 * 3;
	    int * a = new int[size];
	    for (int i = 0; i < size; i += 1024) {
	        a[i] = i + 1;
	    }
	    int aa, bb;
	    while (in >> aa >> bb, aa + bb) {
	        out << aa + bb << endl;
	    }
	}
};
