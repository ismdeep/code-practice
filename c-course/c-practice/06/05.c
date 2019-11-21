#include <stdio.h>
#include <stdlib.h>

#define N 10

int main()
{
    int a[10];

    /* 输入 */
    for (int i = 0; i < N; ++i)
    {
        scanf("%d", &a[i]);
    }

    /* 排序 */
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

    /* 输出 */
    for (int i = 0; i < N; ++i)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
