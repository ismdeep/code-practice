## 实训八实训题目参考代码




### 第1题

用指针变量实现交换变量的值。

```c
#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
    int t;
    t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int a, b;
    scanf("%d%d", &a, &b);
    printf("a = %d    b = %d\n", a, b);
    swap(&a, &b);
    printf("a = %d    b = %d\n", a, b);
    return 0;
}

```
### 第2题

用指针实现:有 n 个整数，使前面各数顺序后移 m 个位置，最后 m 个数变成最前面 m 个数，写一函数完成以上功能，在主函数中输入 n 个整数和输出 调整后的 n 个数。

**题解：** 移动 m 个位置，倒不如直接执行m次 “所有数据往后移动一位”。

```c
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

```




