//
// Created by ismdeep on 2019/4/4.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

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
    return '<';
}


struct BigInt {
    int length;
    int top;
    short sign; /* 0+ 1- */
    int *data;
};

void free_bigint(struct BigInt *bigint) {
    free(bigint->data);
    free(bigint);
}

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
    int len = (int) strlen(str);

    bigint->sign = 0;
    if ('-' == str[0]) { bigint->sign = 1; }
    bigint->data = (int *) malloc(sizeof(int) * (len / 4 + 2));
    memset(bigint->data, 0, sizeof(int) * (len / 4 + 2));
    bigint->length = len / 4 + 2;
    bigint->top = -1;
    int stop = bigint->sign == 1 ? 0 : -1;

    for (int i = len - 1; i > stop; i -= 4) {
        ++bigint->top;
        bigint->data[bigint->top] = 0;
        int from = i - 3 > stop + 1 ? i - 3 : stop + 1;
        for (int j = from; j <= i; ++j) {
            bigint->data[bigint->top] *= 10;
            bigint->data[bigint->top] += (str[j] - '0');
        }
    }


    /* special judge for -0 */
    if (0 == bigint->top && 0 == bigint->data[0]) {
        bigint->sign = 0;
    }

    while (bigint->top > 0 && bigint->data[bigint->top] == 0) --bigint->top;

    return bigint;
}

struct BigInt *bigint_abs(const struct BigInt *bigint_a) {
    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->top = bigint_a->top;
    ans->sign = 0;
    ans->length = bigint_a->length;
    ans->data = (int *) malloc(sizeof(int) * bigint_a->length);
    memset(ans->data, 0, sizeof(int) * bigint_a->length);
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

struct BigInt *bigint_add(const struct BigInt *a, const struct BigInt *b);

struct BigInt *bigint_subtract(const struct BigInt *a, const struct BigInt *b) {
    if (a == b) return create_bigint(0);
    if (0 == bigint_compare(a, b)) return create_bigint(0);

    if (0 == a->sign && 1 == b->sign) {
        struct BigInt *ans = bigint_add(a, bigint_abs(b));
        return ans;
    }

    if (1 == a->sign && 0 == b->sign) {
        struct BigInt *ans = bigint_add(bigint_abs(a), b);
        ans->sign = 1;
        return ans;
    }

    if (1 == a->sign && 1 == b->sign) {
        struct BigInt *ans = bigint_subtract(bigint_abs(b), bigint_abs(a));
//        ans->sign = 1 - ans->sign;
        return ans;
    }

    if (-1 == bigint_compare(a, b)) {
        struct BigInt *ans = bigint_subtract(b, a);
        ans->sign = 1;
        return ans;
    }

    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->length = a->length;
    ans->data = (int *) malloc(sizeof(int) * ans->length);
    ans->sign = 0;
    memset(ans->data, 0, sizeof(int) * ans->length);

    /* copy data ans subtract */
    for (int i = 0; i <= a->top; ++i) {
        ans->data[i] = a->data[i];
    }
    for (int i = 0; i <= b->top; ++i) {
        ans->data[i] -= b->data[i];
    }

    /* arrange data */
    for (int i = 0; i < ans->length - 1; ++i) {
        while (ans->data[i] < 0) {
            --ans->data[i + 1];
            ans->data[i] += MOD;
        }
    }

    ans->top = ans->length - 1;
    while (ans->top > 0 && ans->data[ans->top] == 0) --ans->top;

    return ans;
}

struct BigInt *bigint_add(const struct BigInt *a, const struct BigInt *b) {
    if (1 == a->sign && 1 == b->sign) {
        struct BigInt *ans = bigint_add(bigint_abs(a), bigint_abs(b));
        ans->sign = 1;
        return ans;
    }

    if (1 == a->sign && 0 == b->sign) {
        struct BigInt *ans = bigint_subtract(b, bigint_abs(a));
        return ans;
    }

    if (0 == a->sign && 1 == b->sign) {
        struct BigInt *ans = bigint_subtract(a, bigint_abs(b));
        return ans;
    }

    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->length = a->top > b->top ? a->top + 3 : b->top + 3;
    ans->data = (int *) malloc(sizeof(int) * ans->length);
    ans->sign = 0;
    memset(ans->data, 0, sizeof(int) * ans->length);
    ans->top = -1;

    /* copy and block add */
    for (int i = 0; i <= a->top; ++i) {
        ans->data[i] = a->data[i];
    }
    for (int i = 0; i <= b->top; ++i) {
        ans->data[i] += b->data[i];
    }

    /* arrange data */
    for (int i = 0; i < ans->length - 1; ++i) {
        ans->data[i + 1] += ans->data[i] / MOD;
        ans->data[i] %= MOD;
    }
    ans->top = ans->length - 1;
    while (ans->top > 0 && ans->data[ans->top] == 0) --ans->top;
    return ans;
}

char *bigint_2_string(const struct BigInt *bigint);
struct BigInt *bigint_multiply(const struct BigInt *a, const struct BigInt *b) {
    printf("%s * %s == ", bigint_2_string(a), bigint_2_string(b));
    struct BigInt *zero = create_bigint(0);
    if (bigint_compare(zero, a) * bigint_compare(zero, b) == 0) {
        return zero;
    }

    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->length = a->length + b->length;
    ans->sign = (a->sign + b->sign) % 2;
    ans->data = (int *) malloc(sizeof(int) * (ans->length));
    memset(ans->data, 0, sizeof(int) * ans->length);
    /* @todo deal with the multiplication process */
    for (int i = 0; i <= a->top; ++i) {
        for (int j = 0; j <= b->top; ++j) {
            ans->data[i+j] += a->data[i] * b->data[j];
        }
        for (int j = 0; j < ans->length - 1; ++j) {
            ans->data[j + 1] += ans->data[j] / MOD;
            ans->data[j] %= MOD;
        }
    }

    ans->top = ans->length - 1;
    while (ans->top > 0 && ans->data[ans->top] == 0) --ans->top;
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
    if (bigint->sign == 1) {
        stop = 1;
        ++top;
        data[0] = '-';
    }
    for (int i = 0; i <= bigint->top; ++i) {
        int val = bigint->data[i];
        for (int timeid = 0; timeid < 4; ++timeid) {
            if (top >= stop) {
                data[top--] = (char) ('0' + (val % 10));
                val /= 10;
            }
        }
    }
    return data;
}
