/*
gcc 01-gendata.c -o 01-gendata && 01-gendata > in.txt && type in.txt && gcc -fexec-charset=GBK 03.c -o 03 && 03 < in.txt
*/
#include <stdio.h>

int main()
{
    int a[20];
    int max_id, min_id;

    for (int i = 0; i < 20; ++i)
    {
        scanf("%d", &a[i]);
    }

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

    printf("min_value: a[%d] = %d\n", min_id, a[min_id]);
    printf("max_value: a[%d] = %d\n", max_id, a[max_id]);

    return 0;
}
