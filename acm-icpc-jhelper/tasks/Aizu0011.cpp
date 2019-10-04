#include "../library/header.hpp"
#include "../library/array.hpp"

class Aizu0011 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int w;
	    int n;
	    int left;
	    int right;
	    int tmp;
	    string str;
	    in >> w >> n;
	    int* a = (int*)create_1d_arr(w + 1, sizeof(int));
	    for (int i = 1; i <= w; ++i) {
	        a[i] = i;
	    }
	    while (n--) {
	        in >> str;
	        sscanf(str.data(), "%d,%d", &left, &right);
	        tmp = a[left];
	        a[left] = a[right];
	        a[right] = tmp;
	    }
	    for (int i = 1; i <= w; ++i) {
	        out << a[i] << endl;
	    }
	}
};
