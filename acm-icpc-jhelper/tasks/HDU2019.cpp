#include "../library/header.hpp"

class HDU2019 {
public:
    void solve(std::istream& in, std::ostream& out) {
        int n, x, tmp;
        bool flag = true;
        bool is_first = true;
        while (in >> n >> x, n + x) {
            flag = true;
            is_first = true;
            while (n--) {
                in >> tmp;
                if (tmp >= x && flag) {
                    if (!is_first) {
                        out << " ";
                    }
                    is_first = false;
                    out << x;
                    flag = false;
                }
                if (!is_first) {
                    out << " ";
                }
                is_first = false;
                out << tmp;
            }
            out << endl;
        }
    }
};
