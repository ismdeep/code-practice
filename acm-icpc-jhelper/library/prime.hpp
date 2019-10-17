#include "header.hpp"
#include "array.hpp"

bool *generate_is_prime_table(uint64_t top_value) {
    uint64_t size = top_value + 1;
    bool *is_prime = (bool *) malloc(sizeof(bool) * size);
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

class PrimeTable {
public:
    uint64_t size;
    uint64_t top_value;
    uint64_t *data;

    PrimeTable();

    PrimeTable(uint64_t);

    static PrimeTable generate(uint64_t);
};

PrimeTable::PrimeTable() {}

PrimeTable::PrimeTable(uint64_t top_value) {
    this->top_value = top_value;
    this->data = (uint64_t *) create_array(top_value, sizeof(uint64_t));
}

PrimeTable PrimeTable::generate(uint64_t top_value) {
    PrimeTable prime_table(top_value);
    bool *is_prime = (bool *) generate_is_prime_table(top_value);
    prime_table.size = 0;
    for (uint64_t i = 0; i < top_value; i++) {
        if (is_prime[i]) {
            prime_table.data[prime_table.size] = i;
            ++prime_table.size;
        }
    }
    return prime_table;
}


