#include <stdio.h>
#include <stdlib.h>

int main()
{
    long s = 1;
    for (int i = 1; i <= 10; i++)
    {
        s *= i;
    }
    printf("%d\n", s);
    return 0;
}
