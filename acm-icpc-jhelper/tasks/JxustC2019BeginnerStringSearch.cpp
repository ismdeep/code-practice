#include "../library/header.hpp"

class JxustC2019BeginnerStringSearch {
public:
    void solve(std::istream &in, std::ostream &out) {
        string str1, str2;
        getline(in, str1);
        getline(in, str2);
        int position = str1.find(str2);
        if (-1 == position) {
            transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
            transform(str2.begin(), str2.end(), str2.begin(), ::tolower);
            position = str1.find(str2);
        }
        if (-1 != position) {
            ++position;
        }
        out << position << endl;
    }
};
