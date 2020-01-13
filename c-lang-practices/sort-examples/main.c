#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

bool cmp(const void *data_left, const void *data_right) {
    return *((double *) data_left) <= *((double *) data_right);
}

void select_sort(const void *data_start, const void *data_end, size_t item_size,
                 bool (*cmp_func)(const void *, const void *)) {
    void *left = (void *) data_start;
    while (left < data_end) {
        void *min_p = left;
        void *cur = min_p + item_size;
        while (cur < data_end) {
            if (!cmp_func(min_p, cur)) {
                min_p = cur;
            }
            cur += item_size;
        }
        void *tmp = malloc(item_size);
        memcpy(tmp, left, item_size);
        memcpy(left, min_p, item_size);
        memcpy(min_p, tmp, item_size);
        free(tmp);
        left = left + item_size;
    }
}

int main() {
    srandom((unsigned) time(NULL));
    double a[10];
    for (int i = 0; i < 10; i++) {
        a[i] = (double) (random() % 1000);
    }

    for (int i = 0; i < 10; i++) {
        printf("%.2lf ", a[i]);
    }
    printf("\n");

    select_sort(a, a + 10, sizeof(double), cmp);

    for (int i = 0; i < 10; i++) {
        printf("%.2lf ", a[i]);
    }
    printf("\n");

    return 0;
}
