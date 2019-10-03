#include "../library/header.hpp"


char caesar_cipher_decode(char ch, int key) {
    if ('a' <= ch && ch <= 'z') {
        int val = ch - 'a';
        val = (val + 26 - key) % 26;
        return 'a' + val;
    } else {
        return ch;
    }
}

string decode_string(const string& str, int key) {
    string ans = str;
    for(int i = 0; i < str.length(); ++i) {
        ans[i] = caesar_cipher_decode(str[i], key);
    }
    return ans;
}

class Aizu0017 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    string str;
	    while (getline(in, str)) {
	        TIMES(key_id, 26) {
	            string plain_text = decode_string(str, key_id);
	            if ((int)plain_text.find("the") >= 0 || (int)plain_text.find("this") >= 0 || (int)plain_text.find("that") >= 0) {
	                out << plain_text << endl;
                    break;
	            }
	        }
	    }
	}
};
