#include "../library/header.hpp"

class HDU6536 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int n;
        string str;
        while (in >> n >> str) {
            int x1 = 0;
            int x2 = 0;
            int x3 = 0;
            int x4 = 0;
            int x5 = 0;
            int cnt = 0;
            TIMES(i, n) {
                if (str[i] == 'x') x1++;
                if (str[i] == 't' && x2 < x1) x2++;
                if (str[i] == 'C' && x3 < x2) x3++;
                if (str[i] == 'p' && x4 < x3) x4++;
                if (str[i] == 'c' && x5 < x4) x5++;
                if (x1 && x2 && x3 && x4 && x5) {
                    cnt++;
                    x1--;
                    x2--;
                    x3--;
                    x4--;
                    x5--;
                }
            }
            out << cnt << endl;
        }
    }
};
