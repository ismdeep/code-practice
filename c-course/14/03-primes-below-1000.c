#include <stdio.h>
#include <stdbool.h>

int main()
{
    int v, i;
    bool is_prime;
    for (v = 2; v <= 1000; v++)
    {
        is_prime = true;
        for (i = 2; i < v; i++)
        {
            if (v % i == 0)
            {
                is_prime = false;
            }
        }
        if (is_prime)
        {
            printf("%d ", v);
        }
    }
    return 0;
}