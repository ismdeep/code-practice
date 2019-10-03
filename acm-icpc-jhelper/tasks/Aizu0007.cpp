#include <iostream>

class Aizu0007 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int n;
        in >> n;
        int val = 100000;
        for (int i = 0; i < n; i++) {
            val *= 1.05;
            if (val % 1000 != 0)val = (val / 1000 + 1) * 1000;
        }
        out << val << std::endl;
    }
};
