#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

/* 判断是否为素数的函数 */
bool is_prime(int val)
{
    if (val <= 1)
    {
        return false;
    }
    int stop = sqrt(val);
    for (int i = 2; i <= stop; i++)
    {
        if (0 == val % i)
        {
            return false;
        }
    }
    return true;
}

int main(int argc, char const *argv[])
{
    int primes[1000];
    int cnt = 0;

    /* 1. 一次判断是否是素数，并加入到 primes 数组中 */
    for (int i = 2; i <= 1000; i++)
    {
        if (is_prime(i))
        {
            primes[cnt] = i;
            ++cnt;
        }
    }

    /* 2. 输出结果 */
    printf("素数个数：%d\n", cnt);
    for (int i = 0; i < cnt; ++i)
    {
        printf("%d ", primes[i]);
    }
    printf("\n");

    return 0;
}
