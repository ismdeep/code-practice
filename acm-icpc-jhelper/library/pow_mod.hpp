uint64_t pow_mod(uint64_t a, uint64_t n, uint64_t mod_val) {
    if (n <= 0) {
        return 1;
    }
    if (n == 1) {
        return a % mod_val;
    }
    uint64_t tmp = pow_mod(a, n / 2, mod_val);
    tmp *= tmp;
    tmp %= mod_val;
    tmp *= pow_mod(a, n % 2, mod_val);
    tmp %= mod_val;
    return tmp;
}