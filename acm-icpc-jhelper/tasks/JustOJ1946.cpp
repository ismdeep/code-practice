#include "../library/header.hpp"

class JustOJ1946 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n, m;
	    while (in >> n >> m, n+m) {
	        int *a = (int *) malloc((n + 1) * sizeof(int));
	        TIMES(i, n) {
	            in >> a[i];
	        }
	        a[n] = m;
	        sort(a, a + n + 1);
	        TIMES(i, n + 1) {
	            out << a[i] << " ";
	        }
	        out << endl;
	    }
	}
};
