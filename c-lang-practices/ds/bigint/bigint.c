//
// Created by ismdeep on 2019/4/4.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MOD 10000

int digital_count(int val) {
    int cnt = 0;
    while (val) {
        ++cnt;
        val /= 10;
    }
    if (0 == cnt) ++cnt;
    return cnt;
}


char compare_sign(int val) {
    if (0 == val) return '=';
    if (val > 0) return '>';
    if (val < 0) return '<';
}


struct BigInt {
    int length;
    int top;
    short sign; /* 0+ 1- */
    int *data;
};

struct BigInt *create_bigint(int val) {
    struct BigInt *bigint;
    bigint = (struct BigInt *) malloc(sizeof(struct BigInt));
    bigint->data = (int *) malloc(sizeof(int) * 100);
    memset(bigint->data, 0, 100 * sizeof(int));
    bigint->length = 100;
    bigint->sign = 0;
    if (val < 0) {
        bigint->sign = 1;
        val = 0 - val;
    }
    bigint->top = -1;
    while (val) {
        ++bigint->top;
        bigint->data[bigint->top] = val % MOD;
        val /= MOD;
    }
    if (bigint->top == -1) {
        bigint->top = 0;
        bigint->data[bigint->top] = 0;
    }
    return bigint;
}

struct BigInt *create_bigint_from_str(const char str[]) {
    struct BigInt *bigint;
    bigint = (struct BigInt *) malloc(sizeof(struct BigInt));
    int len = strlen(str);

    bigint->sign = 0; if ('-' == str[0]) { bigint->sign = 1; }
    bigint->data = (int *) malloc(sizeof(int) * (len / 4 + 2));
    bigint->length = len / 4 + 2;
    bigint->top = -1;
    int stop = bigint->sign == 1 ? 0 : -1;

    for (int i = len - 1; i > stop; i -= 4) {
        ++bigint->top;
        bigint->data[bigint->top] = 0;
        int from = i - 3 > stop + 1 ? i - 4 : stop + 1;
        for (int j = from; j <= i; ++j) {
            bigint->data[bigint->top] *= 10;
            bigint->data[bigint->top] += (str[j] - '0');
        }
    }
    return bigint;
}

struct BigInt *bigint_abs(const struct BigInt *bigint_a) {
    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->top = bigint_a->top;
    ans->sign = 0;
    ans->length = bigint_a->length;
    ans->data = (int *) malloc(sizeof(int) * bigint_a->length);
    for (int i = 0; i < ans->length; ++i) {
        ans->data[i] = bigint_a->data[i];
    }
    return ans;
}

int bigint_compare(const struct BigInt *a, const struct BigInt *b) {
    if (a == b) return 0;
    if (a->sign == 0 && b->sign == 1) {
        return 1;
    }
    if (a->sign == 1 && b->sign == 0) {
        return -1;
    }

    if (a->sign == 1 && b->sign == 1) {
        return 0 - bigint_compare(bigint_abs(a), bigint_abs(b));
    }

    if (a->top > b->top) return 1;
    if (a->top < b->top) return -1;
    for (int i = a->top; i >= 0; --i) {
        if (a->data[i] > b->data[i]) return 1;
        if (a->data[i] < b->data[i]) return -1;
    }

    return 0;
}

struct BigInt *bigint_add(struct BigInt *a, struct BigInt *b) {
    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    return ans;
}

char *bigint_2_string(const struct BigInt *bigint) {
    int data_size = ((bigint->top + 1) * 4 + 2);
    char *data = (char *) malloc(sizeof(char) * data_size);
    for (int i = 0; i < data_size; ++i) data[i] = '\0';
    int top = -1 + (bigint->top + 1) * 4;
    top -= (4 - digital_count(bigint->data[bigint->top]));
    data[top + 1] = '\0';
    int stop = 0;
    if (bigint->sign == 1) { stop = 1; ++top; data[0] = '-'; }
    for (int i = 0; i <= bigint->top; ++i) {
        int val = bigint->data[i];
        for (int timeid = 0; timeid < 4; ++timeid) {
            if (top >= stop) { data[top--] = '0' + (val % 10); val /= 10; }
        }
    }
    return data;
}



void print_bigint(const struct BigInt *bigint) {
    printf("%p => %s\n", bigint, bigint_2_string(bigint));
}


void test_compare(const struct BigInt *a, const struct BigInt *b) {
    printf("%s %c %s\n", bigint_2_string(a), compare_sign(bigint_compare(a, b)), bigint_2_string(b));
}


int main(int argc, char *argv[]) {
    struct BigInt *bigint_a = create_bigint(2309847);
    printf("bigint_a => %p\noutput: {%s}\nexpect: {2309847}\n\n", bigint_a, bigint_2_string(bigint_a));

    struct BigInt *bigint_b = create_bigint(-2309847);
    printf("bigint_b => %p\noutput: {%s}\nexpect: {-2309847}\n\n", bigint_b, bigint_2_string(bigint_b));

    struct BigInt *bigint_c = create_bigint_from_str("23974997920438");
    printf("bigint_c => %p\noutput: {%s}\nexpect: {23974997920438}\n\n", bigint_c, bigint_2_string(bigint_c));

    struct BigInt *bigint_d = create_bigint_from_str("-23974997920438");
    printf("bigint_d => %p\noutput: {%s}\nexpect: {-23974997920438}\n\n", bigint_d, bigint_2_string(bigint_d));

    struct BigInt *bigint_e = create_bigint_from_str("10000000");
    printf("bigint_e => %p\noutput: {%s}\nexpect: {10000000}\n\n", bigint_e, bigint_2_string(bigint_e));

    test_compare(bigint_a, bigint_a);
    test_compare(bigint_a, bigint_b);
    test_compare(bigint_a, bigint_c);
    test_compare(bigint_a, bigint_d);
    test_compare(bigint_b, bigint_c);
    test_compare(bigint_b, bigint_d);
    test_compare(bigint_c, bigint_d);
    test_compare(bigint_d, bigint_c);
    return 0;
}