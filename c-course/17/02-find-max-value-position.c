#include <stdio.h>

int main()
{
    int a[100];
    int n, i, m;
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    m = 0;
    for (i = 1; i < n; i++)
    {
        if (a[i] > a[m])
        {
            m = i;
        }
    }

    printf("a[%d] = %d\n", m, a[m]);
    return 0;
}
