#include <stdio.h>
#include <stdlib.h>

#define N 10


void print_arr(int *a, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
}


int main()
{
    int a[20];
    int val;

    /* 1. 输入 */
    for (int i = 0; i < N; ++i)
    {
        scanf("%d", &a[i]);
    }

    /* 2. 排序 */
    for (int left = 0; left <= N - 2; left++)
    {
        int min_id = left;
        for (int i = left + 1; i < N; i++)
        {
            if (a[i] < a[min_id])
            {
                min_id = i;
            }
        }
        int t     = a[left];
        a[left]   = a[min_id];
        a[min_id] = t;
    }

    /* 3. 输出排序后 */
    printf("排序后的数列： ");
    print_arr(a, N);
    printf("\n");

    /* 4. 再输入一个数字 */
    scanf("%d", &val);
    printf("输入的数字为：%d\n", val);

    for (int i = 0; i < N; i++)
    {
        if (a[i] == val)
        {
            /* 找到相同的数字，执行删除操作。 */
            printf("输入的数字在数列中找到相同的数字，执行删除操作。\n");
            for (int j = i + 1; j < N; j++)
            {
                a[j-1] = a[j];
            }
            print_arr(a, N - 1);
            return 0;
        }

        if (a[i] > val)
        {
            /* 找到比 val 大的数字，执行插入操作。 */
            printf("输入的数字在数列中并不存在，执行插入操作。\n");
            for (int j = N - 1; j >= i; j--)
            {
                a[j+1] = a[j];
            }
            a[i] = val;
            print_arr(a, N + 1);
            return 0;
        }
    }

    /* 如果能执行到此处，说明整个数组里面都没有找到一个比 val 大的，则在末尾增加 val */
    a[N] = val;
    printf("输入的数字是全局最大的。");
    printf("输入的数字在数列中并不存在，执行插入操作。\n");
    print_arr(a, N + 1);
    
    return 0;
}
