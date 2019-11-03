#include "../library/header.hpp"

int char_type(char ch) {
    if (('A' <= ch && ch <= 'Z') || ('a' <= ch && ch <= 'z')) {
        return 0;
    }
    if ('0' <= ch && ch <= '9') {
        return 1;
    }
    if (' ' == ch) {
        return 2;
    }
    return 3;
}

class DOTCPP1012 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string str;
	    int a[4] = {0,0,0,0};
	    getline(in, str);
	    TIMES(i, str.length()) {
	        a[char_type(str[i])]++;
	    }
	    out << a[0] << " " << a[1] << " " << a[2] << " " << a[3] << endl;
	}
};
