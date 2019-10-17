#include "../library/header.hpp"

class DOTCPP1004 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int a[55];
        a[0] = 0;
        a[1] = 1;
        a[2] = 2;
        a[3] = 3;
        FOR (int, i, 4, 54, 1) {
            a[i] = a[i - 1] + a[i - 3];
        }
        int n;
        while (in >>n, n) {
            out << a[n] << endl;
        }
    }
};
