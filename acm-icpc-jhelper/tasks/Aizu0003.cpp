#include "../library/header.hpp"

void swap (int* a, int* b) {
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

void sort_abc(int* a, int* b, int* c) {
    if (*a > *b) swap(a, b);
    if (*a > *c) swap(a, c);
    if (*b > *c) swap(b, c);
}

class Aizu0003 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int t;
	    in >> t;
	    TIMES(tid, t) {
	        int a, b, c;
	        in >> a >> b >> c;
	        sort_abc(&a, &b, &c);
	        if (a * a + b * b == c * c) {
	            out << "YES" << endl;
	        } else {
	            out << "NO" << endl;
	        }
	    }
	}
};
