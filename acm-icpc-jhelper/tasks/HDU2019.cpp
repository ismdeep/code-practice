#include "../library/header.hpp"

class HDU2019 {
public:
    void solve(std::istream& in, std::ostream& out) {
        int n, x, tmp;
        bool flag = true;
        while (in >> n >> x, n + x) {
            flag = true;
            while (n--) {
                in >> tmp;
                if (tmp >= x && flag) {
                    out << x << " ";
                    flag = false;
                }
                out << tmp << " ";
            }
            out << endl;
        }
    }
};
