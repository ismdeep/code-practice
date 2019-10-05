#include "../library/header.hpp"

class Aizu0006 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    std::string str;
	    in >> str;
	    std::string ans;
	    for (int i = str.length() - 1; i >= 0; --i) {
	        ans += str[i];
	    }
	    out << ans << std::endl;
	}
};
