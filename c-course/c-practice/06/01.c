#include <stdio.h>

int main()
{
    int a[20];
    int cnt, sum;

    /* 1. 输入 */
    for (int i = 0; i < 20; ++i)
    {
        scanf("%d", &a[i]);
    }

    /* 2. 依次判定是否是正数 */
    cnt = 0;
    sum = 0;
    for (int i = 0; i < 20; ++i)
    {
        if (a[i] > 0)
        {
            ++cnt;
            sum += a[i];
        }
    }

    /* 3. 输出结果 */
    printf("正数个数为%d, 这些正数的和为%d\n", cnt, sum);

    return 0;
}
