#include "../library/header.hpp"

class DOTCPP1010 {
public:
    void solve(std::istream &in, std::ostream &out) {
        int val;
        in >> val;
        int ans = 0;
        if (val <= 100000) {
            ans = val * 0.1;
        } else if (val <= 200000) {
            ans = (100000 * 0.1) + (val - 100000) * 0.075;
        } else if (val <= 400000) {
            ans = (100000 * 0.1) + 100000 * 0.075 + (val - 200000) * 0.05;
        } else if (val <= 600000) {
            ans = (100000 * 0.1) + 100000 * 0.075 + 200000 * 0.05 + (val - 400000) * 0.03;
        } else if (val <= 1000000) {
            ans = (100000 * 0.1) + 100000 * 0.075 + 200000 * 0.05 + 400000 * 0.03 + (val - 600000) * 0.015;
        } else {
            ans = (100000 * 0.1) + 100000 * 0.075 + 200000 * 0.05 + 400000 * 0.03 + 600000 * 0.015 + (val - 1000000) * 0.01;
        }
        out << ans << endl;
    }
};
