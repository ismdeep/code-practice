#include "../library/header.hpp"

char encrypt_lower(char ch) {
    return 'a' + ((ch - 'a') + 4) % 26;
}

char encrypt_upper(char ch) {
    return 'A' + ((ch - 'A') + 4) % 26;
}

char encrypt(char ch) {
    if ('A' <= ch && ch <= 'Z') {
        return encrypt_upper(ch);
    }

    if ('a' <= ch && ch <= 'z') {
        return encrypt_lower(ch);
    }

    return ch;
}

class DOTCPP1003 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string str;
	    in >> str;
	    TIMES(str_id, str.length()) {
	        str[str_id] = encrypt(str[str_id]);
	    }
	    out << str << endl;
	}
};
