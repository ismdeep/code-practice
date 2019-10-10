#include "../library/header.hpp"

class Aizu0020 {
public:
    void solve(std::istream &in, std::ostream &out) {
        string str;
        getline(in, sstr);
        TIMES(i, str.length()) {
            if ('a' <= str[i] && str[i] <= 'z') {
                str[i] -= 32;
            }
        }
        out << str << endl;
    }
};
