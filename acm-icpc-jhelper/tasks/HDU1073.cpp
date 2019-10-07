#include "../library/header.hpp"

#define MAXN 5050

#define AC "Accepted"
#define PE "Presentation Error"
#define WA "Wrong Answer"

string input(std::istream& in)
{
    int i;
    string ans = "";
    string tmp;
    while (tmp != "START")
    {
        getline(in, tmp);
    }
    while (getline(in, tmp)) {
        if (tmp == "END") break;
        if (tmp.length() != 0) {
            ans += tmp;
        }
        ans += "\n";
    }
    return ans;
}

string beautify(string str) {
    int i ;
    int ans_len;
    ans_len = 0;
    char *ans = (char *)malloc(sizeof(char) * MAXN);
    for (i = 0; i < str.length(); ++i) {
        if (str[i] != ' ' && str[i] != '\t' && str[i] != '\n') {
            ans[ans_len] = str[i];
            ++ans_len;
        }
    }
    ans[ans_len] = '\0';
    return ans;
}

class HDU1073 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int t;
	    in >> t;
	    TIMES(tid, t) {
            string a = input(in);
            string b = input(in);
            if (a == b) {
                out << AC << endl;
            }else if ( beautify(a) == beautify(b)) {
                out <<  PE << endl;
            }else{
                out << WA << endl;
            }
	    }
	}
};
