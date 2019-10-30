#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 2;
    int b = a + (a++);
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    return 0;
}
