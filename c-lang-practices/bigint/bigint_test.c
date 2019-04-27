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

char *run_command(char *cmd) {
    FILE *fin = popen(cmd, "r+");
    char *res = (char *) malloc(sizeof(char) * 1024);
    fscanf(fin, "%s", res);
    pclose(fin);
    return res;
}

bool bigint_create_test(int test_times) {
    TIMES(i, test_times) {
        int val = rand_int(-65535, 65535);
        struct BigInt *bigint_a = create_bigint(val);
        char cmd[65535];
        TIMES(j, 65535) {
            cmd[i] = 'a';
        }
        sprintf(cmd, "python3 -c \"print(%d == %s)\"", val, bigint_2_string(bigint_a));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_create_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(bigint_a);
    }
    return true;
}

bool bigint_create_str_test (int test_times) {
    TIMES(i, test_times) {
        char *str = rand_bigint_str(2, rand_int(1, 30));
        struct BigInt *bigint_a = create_bigint_from_str(str);
        char cmd[65535];
        sprintf(cmd, "python3 -c \"print(int('%s') == int('%s'))\"", str, bigint_2_string(bigint_a));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_create_str_test() => test(%d): SUCCEEDED\n", i + 1);
        free(str);
        free_bigint(bigint_a);
    }
    return true;
}

bool bigint_compare_test(int test_times) {
    TIMES(i, test_times) {
        struct BigInt *bigint_a = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        struct BigInt *bigint_b = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        char cmd[65535];
        sprintf(cmd, "python3 -c \"print(int('%s') %s int('%s'))\"",
                bigint_2_string(bigint_a),
                compare_sign(bigint_compare(bigint_a, bigint_b)),
                bigint_2_string(bigint_b));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_compare_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(bigint_a);
        free_bigint(bigint_b);
    }
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
        struct BigInt *sum = bigint_add(a, b);
        sprintf(cmd, "python3 -c \"print(%s + %s == %s)\"", bigint_2_string(a), bigint_2_string(b), bigint_2_string(sum));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_add_test() => test(%d): SUCCEEDED\n", i + 1);
        free(str_a);
        free(str_b);
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
        struct BigInt *c = bigint_subtract(a, b);
        sprintf(cmd, "python3 -c \'print(%s - %s == %s)\'", bigint_2_string(a), bigint_2_string(b), bigint_2_string(c));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_subtract_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(a);
        free_bigint(b);
        free_bigint(c);
    }
    return true;
}

bool bigint_multiply_test(int test_times) {
    TIMES(i, test_times) {
        struct BigInt *a;
        struct BigInt *b;
        a = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        b = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        char cmd[65535];
        struct BigInt *c = bigint_multiply(a, b);
        sprintf(cmd, "python3 -c \"print(%s * %s == %s)\"", bigint_2_string(a), bigint_2_string(b), bigint_2_string(c));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_multiply_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(a);
        free_bigint(b);
        free_bigint(c);
    }
    return true;
}

bool bigint_divided_by_int_test(int test_times) {
    TIMES(i, test_times) {
        struct BigInt *a;
        int val = 0;
        while (0 == val) {
            val = rand_int(-2147483647, 2147483647);
        }

        a = create_bigint_from_str(rand_bigint_str(2, rand_int(1, 30)));
        char cmd[65535];
        struct BigInt *c = bigint_divided_by_int(a, val);
        sprintf(cmd, "python3 -c \"print(%s // %d == %s)\"", bigint_2_string(a), val, bigint_2_string(c));
        assert(strcmp("True", run_command(cmd)) == 0);
        printf("bigint_divided_by_int_test() => test(%d): SUCCEEDED\n", i + 1);
        free_bigint(a);
        free_bigint(c);
    }
    return true;
}

bool bigint_divided_by_bigint_test(int test_times) {
//    TIMES(i, test_times) {
//
//    }
    return true;
}

int main(int argc, char *argv[]) {
    printf("bigint_create_test() => tests: %s\n", bigint_create_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_create_str_test() => tests: %s\n", bigint_create_str_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_compare_test() => tests: %s\n", bigint_compare_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_add_test() => tests: %s\n", bigint_add_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_subtract_test() => tests: %s\n", bigint_subtract_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_multiply_test() => tests: %s\n", bigint_multiply_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_divided_by_int_test() => tests: %s\n", bigint_divided_by_int_test(300) ? "SUCCEEDED" : "FAILED");
    printf("bigint_divided_by_bigint_test() => tests: %s\n", bigint_divided_by_bigint_test(300) ? "SUCCEEDED" : "FAILED");
    return 0;
}