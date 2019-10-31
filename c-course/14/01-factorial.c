#include <stdio.h>

int main()
{
    int n, i, val;
    scanf("%d", &n);
    val = 1;
    for (i = 1; i <= n; i++)
    {
        val *= i;
    }
    printf("%d! = %d\n", n, val);
    return 0;
}