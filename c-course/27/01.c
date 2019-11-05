#include <stdio.h>

/* 交换两个指针指向的值 */
void swap(int *a, int *b)
{
    int t;
    t  = *a;
    *a = *b;
    *b =  t;
}

/* 在一定范围寻找最大值的位置 */
int max_value_postion(int *a, int n)
{
    int m = 0;
    int i;
    for (i = 1; i < n; i++)
    {
        if (a[i] > a[m])
        {
            m = i;
        }
    }
    return m;
}

/* 在一定范围寻找最小值的位置 */
int min_value_position(int *a, int n)
{
    int m = 0;
    int i;
    for (i = 1; i < n; i++)
    {
        if (a[i] < a[m])
        {
            m = i;
        }
    }
    return m;
}

/* 最简单的选择排序 */
void select_sort(int *a, int n)
{
    int left, t, m, i;

    for (left = 0; left <= n - 2; left++)
    {
        /* 找出 [left ~ n - 1] 最大值的位置 */
        m = max_value_postion(a + left, n - left);

        /* 交换最左边 和 最大值位置的值 */
        swap(&a[left], &a[m]);
    }
}

/* 选择排序之递归版本V1 */
void select_sort_recursive_v1(int *a, int n) 
{
    int m, i, t;
    if (n <= 1) return;

    /* 找最小值，与最后的一个交换。 */
    m = min_value_position(a, n);
    swap(&a[m], &a[n-1]);

    /* 剩下的 n - 1 个进行排序 */
    select_sort_recursive_v1(a, n - 1);
}


/* 选择排序之递归版本V2 */
void select_sort_recursive_v2(int *a, int n)
{
    int m, i, t;
    if (n <= 1) return;

    /* 找最大值，与最前面的交换。 */
    m = max_value_postion(a, n);
    swap(&a[m], &a[0]);

    /* 剩下的 n - 1 个进行排序 */
    select_sort_recursive_v2(a + 1, n - 1);
}


int main()
{
    int n, i, left, m, t;
    int a[100];

    /* 输入 n */
    scanf("%d", &n);

    /* 输入 n 个数字 */
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }


    // select_sort(a, n);
    // select_sort_recursive_v1(a, n);
    select_sort_recursive_v2(a, n);


    /* 输出已排序的 n 个数 */
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
