#include <stdio.h>

int main()
{
    int a[100];
    int n, i, left, m, t;
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for (left = 0; left <= n - 2; left++)
    {
        m = left;
        for (i = left + 1; i < n; i++)
        {
            if (a[i] < a[m])
            {
                m = i;
            }
        }
        t = a[left];
        a[left] = a[m];
        a[m] = t;
    }

    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}