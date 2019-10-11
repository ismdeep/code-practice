#include "../library/header.hpp"

string dict[] = {
        "ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"
};

class PAT1002 {
public:
    void solve(std::istream &in, std::ostream &out) {
        string str;
        in >> str;
        int ans = 0;
        for (int i = 0; i < str.length(); ++i) {
            ans += str[i] - '0';
        }
        stack<int> s;
        while (ans != 0) {
            s.push(ans % 10);
            ans /= 10;
        }
        bool flag = false;
        while (!s.empty()) {
            if (flag) {
                out << " ";
            }
            flag = true;
            out << dict[s.top()];
            s.pop();
        }
        out << endl;
    }
};
