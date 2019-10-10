#include "header.hpp"

bool* generate_is_prime_table(uint64_t top_value) {
    uint64_t size = top_value + 1;
    bool* is_prime = (bool*) malloc(sizeof(bool) * size);
    TIMES(i, size) {
        is_prime[i] = true;
    }
    is_prime[0] = false;
    is_prime[1] = false;
    FOR(uint64_t, i, 0, size, 1) {
        if (is_prime[i]) {
            FOR(uint64_t, j, i * i, size, i) {
                is_prime[j] = false;
            }
        }
    }
    return is_prime;
}
