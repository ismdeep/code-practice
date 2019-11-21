#include <stdio.h>

int main()
{
    int a[20];
    int max_id, min_id;

    /* 1. 输入数据 */
    for (int i = 0; i < 20; ++i)
    {
        scanf("%d", &a[i]);
    }

    /* 2. 寻找最大值和最小值的位置 */
    max_id = 0;
    min_id = 0;
    for (int i = 1; i < 20; ++i)
    {
        if (a[i] > a[max_id])
        {
            max_id = i;
        }
        if (a[i] < a[min_id])
        {
            min_id = i;
        }
    }

    /* 3. 输出结果 */
    printf("min_value: a[%d] = %d\n", min_id, a[min_id]);
    printf("max_value: a[%d] = %d\n", max_id, a[max_id]);

    return 0;
}
