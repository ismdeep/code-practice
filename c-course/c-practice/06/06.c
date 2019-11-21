#include <stdio.h>

int main()
{
    int a[4][5];

    /* 1. 输入数据 */
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    int max_i, max_j;
    int min_i, min_j;

    /* 2. 寻找最大值和最小值的位置 */
    max_i = 0;
    max_j = 0;
    min_i = 0;
    min_j = 0;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (a[i][j] > a[max_i][max_j])
            {
                max_i = i;
                max_j = j;
            }
            if (a[i][j] < a[min_i][min_j])
            {
                min_i = i;
                min_j = j;
            }
        }
    }

    /* 3. 输出最小值和最大值的位置以及值 */
    printf("min_value: a[%d][%d] = %d\n", min_i, min_j, a[min_i][min_j]);
    printf("max_value: a[%d][%d] = %d\n", max_i, max_j, a[max_i][max_j]);

    return 0;
}
