#include "../library/header.hpp"
#include "../library/kmp.hpp"

class TestKMP {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string main_str;
	    string pattern_str;
	    in >> main_str >> pattern_str;
	    KMP kmp;
	    kmp.set_main_string(main_str);
	    kmp.set_pattern(pattern_str);
	    out << kmp.get_pattern_in_main() << endl;
	}
};


