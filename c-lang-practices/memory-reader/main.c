#include <stdio.h>


void read_memory(unsigned char *start_address, size_t size) {
    unsigned char *cursor = start_address;
    for (size_t i = 0; i < size; i++) {
        printf("%02X ", *cursor);
        ++cursor;
    }
}

int main() {
    long double a = 1;
    read_memory((unsigned char *) &a, sizeof(a));

    return 0;
}
