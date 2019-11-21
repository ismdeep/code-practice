#include <stdio.h>
#include <stdbool.h>

bool is_perfect_number(int n)
{
    int sum = 0;
    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }
    return sum == n;
}


int main()
{
    for (int val = 1; val <= 1000; val++)
    {
        if(is_perfect_number(val))
        {
            printf("%d\n", val);
        }
    }
    return 0;
}
