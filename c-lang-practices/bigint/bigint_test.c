//
// Created by ismdeep on 2019-04-14.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <bigint.h>
#include <rand_util.h>
#include <unistd.h>

#define TIMES(id, n) for (int id = 0; id < (n); ++id)

bool bigint_create_test(int test_times) {
    TIMES(i, test_times) {
        int val = rand_int(-65535, 65535);
        struct BigInt *bigint_a = create_bigint(val);
        char cmd[65535];
        memset(cmd, 0, sizeof(char) * 65535);
        sprintf(cmd, "python3 -c \"print(%d == %s)\"", val, bigint_2_string(bigint_a));
        FILE *fin = popen(cmd, "r+");
        char res[1024];
        memset(res, 0, sizeof(char) * 1024);
        fscanf(fin, "%s", res);
        pclose(fin);
        assert(strcmp("True", res) == 0);
        printf("bigint_create_test() => test(%d): SUCCEEDED\n", i + 1);
    }
    return true;
}

bool bigint_create_str_test (int test_times) {
    TIMES(i, test_times) {
        char *str = rand_bigint_str(2, rand_int(1, 30));
        struct BigInt *bigint_a = create_bigint_from_str(str);
        char cmd[65535];
        memset(cmd, 0, sizeof(char) * 65535);
        sprintf(cmd, "python3 -c \"print(int('%s') == int('%s'))\"", str, bigint_2_string(bigint_a));
        FILE *fin = popen(cmd, "r+");
        char res[1024];
        memset(res, 0, sizeof(char) * 1024);
        fscanf(fin, "%s", res);
        pclose(fin);
        assert(strcmp("True", res) == 0);
        printf("bigint_create_str_test() => test(%d): SUCCEEDED\n", i + 1);
        free(str);
    }
    return true;
}

bool bigint_compare_test() {
    struct BigInt *bigint_zero = create_bigint_from_str("-0");
    assert(strcmp("0", bigint_2_string(bigint_zero)) == 0);

    struct BigInt *bigint_a = create_bigint(2309847);
    assert(strcmp("2309847", bigint_2_string(bigint_a)) == 0);

    struct BigInt *bigint_b = create_bigint(-2309847);
    assert(strcmp("-2309847", bigint_2_string(bigint_b)) == 0);

    struct BigInt *bigint_c = create_bigint_from_str("23974997920438");
    assert(strcmp("23974997920438", bigint_2_string(bigint_c)) == 0);

    struct BigInt *bigint_d = create_bigint_from_str("-23974997920438");
    assert(strcmp("-23974997920438", bigint_2_string(bigint_d)) == 0);

    struct BigInt *bigint_e = create_bigint_from_str("10000000");
    assert(strcmp("10000000", bigint_2_string(bigint_e)) == 0);

    assert(bigint_compare(bigint_a, bigint_a) == 0);
    assert(bigint_compare(bigint_a, bigint_b) == 1);
    assert(bigint_compare(bigint_a, bigint_c) == -1);
    assert(bigint_compare(bigint_a, bigint_d) == 1);
    assert(bigint_compare(bigint_a, bigint_e) == -1);

    return true;
}

bool bigint_add_test(int test_times) {
    TIMES(i, test_times) {
        struct BigInt *a;
        struct BigInt *b;
        char *str_a = rand_bigint_str(2, rand_int(1, 30));
        char *str_b = rand_bigint_str(2, rand_int(1, 30));
        a = create_bigint_from_str(str_a);
        b = create_bigint_from_str(str_b);
        char cmd[65535];
        memset(cmd, 0, sizeof(char) * 65535);
        struct BigInt *sum = bigint_add(a, b);
        sprintf(cmd, "python3 -c \"print(%s + %s == %s)\"", bigint_2_string(a), bigint_2_string(b), bigint_2_string(sum));
        FILE *fin = popen(cmd, "r+");
        char res[1024];
        memset(res, 0, sizeof(char) * 1024);
        fscanf(fin, "%s", res);
        pclose(fin);

//        printf("%s => %s\n", str_a, bigint_2_string(a));
//        printf("%s => %s\n", str_b, bigint_2_string(b));
//        printf("%s\n", bigint_2_string(sum));
//        printf("%s\n", cmd);

        assert(strcmp("True", res) == 0);
        printf("bigint_add_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(a);
        free_bigint(b);
        free_bigint(sum);
    }
    return true;
}


bool bigint_subtract_test(int test_times) {
    TIMES(i, test_times) {
        struct BigInt *a;
        struct BigInt *b;
        a = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        b = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        char cmd[65535];
        memset(cmd, 0, sizeof(char) * 65535);
        struct BigInt *c = bigint_subtract(a, b);
        sprintf(cmd, "python3 -c \'print(%s - %s == %s)\'", bigint_2_string(a), bigint_2_string(b), bigint_2_string(c));
        FILE *fin = popen(cmd, "r");
        char res[1024];
        memset(res, 0, sizeof(char) * 1024);
        fscanf(fin, "%s", res);
        pclose(fin);
        assert(strcmp("True", res) == 0);
        printf("bigint_subtract_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(a);
        free_bigint(b);
        free_bigint(c);
    }
    return true;
}


int main(int argc, char *argv[]) {
    printf("bigint_create_test() => tests: %s\n", bigint_create_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_create_str_test() => tests: %s\n", bigint_create_str_test(300) ? "SUCCEEDED" : "FAILED");
//    printf("bigint_compare_test() => tests: %s\n", bigint_compare_test() ? "SUCCEEDED" : "FAILED");
    printf("bigint_add_test() => tests: %s\n", bigint_add_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_subtract_test() => tests: %s\n", bigint_subtract_test(300) ? "SUCCEEDED" : "FAILED");

    return 0;
}