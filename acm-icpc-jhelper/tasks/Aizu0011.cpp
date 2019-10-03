#include "../library/header.hpp"

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
	    int* a = (int*) malloc(sizeof(int) * (w + 1));
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
