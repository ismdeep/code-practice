#include <stdio.h>
#include <stdlib.h>

void move_data_one(int *data, int n) {
    int tmp = data[n-1];
    for (int i = n - 1; i >= 1; i--) {
        data[i] = data[i-1];
    }
    data[0] = tmp;
}

void move_data(int *data, int n, int move_step) {
    while (move_step--) {
        move_data_one(data, n);
    }
}

void show_arr(const int *data, int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        if (i != 0) {
            printf(" ");
        }
        printf("%d", data[i]);
    }
    printf("]\n");
}

int main() {
    int n, m;
    int *a;
    scanf("%d", &n);
    a = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    scanf("%d", &m);

    show_arr(a, n);
    move_data(a, n, m);
    show_arr(a, n);

    return 0;
}
