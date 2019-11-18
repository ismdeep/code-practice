#include "../library/header.hpp"

#define MOD 20191117

uint64_t pow_mod(uint64_t a, uint64_t b, uint64_t mod) {
    uint64_t ans = 1;
    while (b) {
        if (b & 1) {
            ans = ans * a % mod;
        }
        a = a * a % mod;
        b >>= 1;
    }
    return ans;
}

class JxustC2019ProInfinitePro {
public:
    void solve(std::istream &in, std::ostream &out) {
        uint64_t a[50] = {0, 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423,
                          9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433,
                          1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011};
        uint64_t n;
        in >> n;
        out << (pow_mod(2, a[n] - 1, MOD) + MOD - 1 ) % MOD << endl;
    }
};
