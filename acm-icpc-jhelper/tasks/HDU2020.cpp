#include "../library/header.hpp"
#include "../library/array.hpp"

bool abs_cmp(int a, int b) {
    return abs(a) > abs(b);
}

class HDU2020 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    uint64_t n;
	    while (in >> n, n) {
	        int* arr = (int*) create_array(n, sizeof(int));
	        TIMES(i, n) {
	            in >> arr[i];
	        }
	        sort(arr, arr + n, abs_cmp);
	        TIMES(i, n) {
	            out << arr[i];
	            if (i + 1 < n) {
	                out << " ";
	            }
	        }
	        out << endl;
	    }
	}
};
