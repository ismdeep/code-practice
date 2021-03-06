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


char *compare_sign(int val) {
    if (0 == val) { return "=="; }
    if (val > 0) return ">";
    return "<";
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

void bigint_arrange(struct BigInt *bigint) {
    bigint->top = bigint->length - 1;
    for (int i = 0; i < bigint->top; ++i) {
        if (bigint->data[i] >= 0) {
            bigint->data[i+1] += (bigint->data[i] / MOD);
            bigint->data[i] %= MOD;
        }else{
            int val = (-bigint->data[i]) / MOD + 1;
            bigint->data[i + 1] -= val;
            bigint->data[i] += (val * MOD);
        }
    }
    while (bigint->data[bigint->top] == 0 && bigint->top > 0) --bigint->top;
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
        struct BigInt *b_abs_val = bigint_abs(b);
        struct BigInt *ans = bigint_add(a, b_abs_val);
        free_bigint(b_abs_val);
        return ans;
    }

    if (1 == a->sign && 0 == b->sign) {
        struct BigInt *a_abs_val = bigint_abs(a);
        struct BigInt *ans = bigint_add(a_abs_val, b);
        ans->sign = 1;
        free_bigint(a_abs_val);
        return ans;
    }

    if (1 == a->sign && 1 == b->sign) {
        struct BigInt *a_abs_val = bigint_abs(a);
        struct BigInt *b_abs_val = bigint_abs(b);
        struct BigInt *ans = bigint_subtract(b_abs_val, a_abs_val);
        free_bigint(a_abs_val);
        free_bigint(b_abs_val);
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

    bigint_arrange(ans);

    return ans;
}

struct BigInt *bigint_add(const struct BigInt *a, const struct BigInt *b) {
    if (1 == a->sign && 1 == b->sign) {
        struct BigInt *a_abs_val = bigint_abs(a);
        struct BigInt *b_abs_val = bigint_abs(b);
        struct BigInt *ans = bigint_add(a_abs_val, b_abs_val);
        ans->sign = 1;
        free_bigint(a_abs_val);
        free_bigint(b_abs_val);
        return ans;
    }

    if (1 == a->sign && 0 == b->sign) {
        struct BigInt *a_abs_val = bigint_abs(a);
        struct BigInt *ans = bigint_subtract(b, a_abs_val);
        free_bigint(a_abs_val);
        return ans;
    }

    if (0 == a->sign && 1 == b->sign) {
        struct BigInt *b_abs_val = bigint_abs(b);
        struct BigInt *ans = bigint_subtract(a, b_abs_val);
        free_bigint(b_abs_val);
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

    bigint_arrange(ans);
    return ans;
}

char *bigint_2_string(const struct BigInt *bigint);
struct BigInt *bigint_multiply(const struct BigInt *a, const struct BigInt *b) {
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
        bigint_arrange(ans);
    }

    bigint_arrange(ans);
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


struct BigInt *bigint_divided_by_int(struct BigInt *bigint, int val) {
    assert(0 != val);

    if (strcmp("0", bigint_2_string(bigint)) == 0) {
        return create_bigint_from_str("0");
    }

    struct BigInt *ans;
    ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->length = bigint->length;
    ans->sign = bigint->sign;
    ans->data = (int *) malloc(sizeof(int) * ans->length);
    long long *data = (long long *) malloc(sizeof(long long) * ans->length);
    memset(     data, 0, sizeof(long long) * ans->length);
    memset(ans->data, 0, sizeof(int) * ans->length);
    ans->top = bigint->top;
    for (int i = 0; i <= ans->top; ++i) {
        data[i] = bigint->data[i];
    }

    if (val < 0) {
        ans->sign = 1 - ans->sign;
        val = -val;
    }

    for (int i = ans->top; i >= 1; --i) {
        data[i-1] += (MOD * (data[i] % val));
        data[i] /= val;
    }
    data[0] /= val;
    if (1 == ans->sign) ++data[0];

    for (int i = 0; i <= ans->top; ++i) {
        data[i+1] += data[i] / MOD;
        data[i] %= MOD;
    }
    ++ans->top;
    while (ans->top > 0 && data[ans->top] == 0) --ans->top;
    for (int i = 0; i <= ans->top; ++i) {
        ans->data[i] = data[i];
    }
    free(data);

    return ans;
}

struct BigInt *bigint_divided_by_bigint(struct BigInt *a, struct BigInt *b) {
    if (a->top < b->top) {
        return create_bigint(0);
    }

    if (a->top == b->top) {
        int left = 0;
        int right = MOD;
        return create_bigint(1);
    }

    struct BigInt *ans = (struct BigInt *) malloc(sizeof(struct BigInt));
    ans->sign = a->sign == b->sign ? 0 : 1;
    ans->top = a->top;
    ans->length = a->length;
    ans->data = (int *) malloc(sizeof(int) * ans->length);
    memset(ans->data, 0, sizeof(int) * ans->length);

    struct BigInt *remainder = (struct BigInt *) malloc(sizeof(struct BigInt));
    remainder->sign = 0;
    remainder->top = 0;
    remainder->length = 1;
    remainder->data = (int *) malloc(sizeof(int) * 1);

    for (int _index_ = a->top; _index_ >= 0; --_index_) {
        struct BigInt *tmp = bigint_multiply(remainder, create_bigint(MOD));
        tmp = bigint_add(tmp, create_bigint(a->data[_index_]));
    }

    return ans;
}