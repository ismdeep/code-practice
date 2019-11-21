/*
gcc 01-gendata.c -o 01-gendata && 01-gendata > in.txt && type in.txt && gcc -fexec-charset=GBK 01.c -o main && main < in.txt
*/
#include <stdio.h>

int main()
{
    int a[20];
    int cnt, sum;

    for (int i = 0; i < 20; ++i)
    {
        scanf("%d", &a[i]);
    }

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

    printf("正数个数为%d, 这些正数的和为%d\n", cnt, sum);

    return 0;
}
