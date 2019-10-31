#include <stdio.h>

int main()
{
    int v, a, b, c, t; /* a,b,c 分别表示v的个位，十位，百位 */
    for (v = 100; v <= 999; v++)
    {
        t = v;
        a = t % 10; t /= 10;
        b = t % 10; t /= 10;
        c = t;
        if (a*a*a + b*b*b + c*c*c == v)
        {
            printf("%d\n", v);
        }
    }
    return 0;
}
