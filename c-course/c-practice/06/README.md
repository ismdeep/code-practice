## 实训六  数据类型构造与模块化程序设计——数组的构造与应用





### 第1题

题目：从键盘输入20 个整型数据，统计其中正数的个数，并计算它们的求和。

```c
/*
gcc 01-gendata.c -o 01-gendata && 01-gendata > in.txt && type in.txt && gcc -fexec-charset=GBK 01.c -o main && main < in.txt
*/
#include <stdio.h>

int main()
{
    int a[20];
    int cnt, sum;

    for (int i = 0; i < 20; ++i)
    {
        scanf("%d", &a[i]);
    }

    cnt = 0;
    sum = 0;
    for (int i = 0; i < 20; ++i)
    {
        if (a[i] > 0)
        {
            ++cnt;
            sum += a[i];
        }
    }

    printf("正数个数为%d, 这些正数的和为%d\n", cnt, sum);

    return 0;
}
```


### 第2题

题目：把 1000 以内的素数存放在数组中，并输出素数的个数和各个素数。

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

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

    for (int i = 2; i <= 1000; i++)
    {
        if (is_prime(i))
        {
            primes[cnt] = i;
            ++cnt;
        }
    }

    printf("素数个数：%d\n", cnt);
    for (int i = 0; i < cnt; ++i)
    {
        printf("%d ", primes[i]);
    }
    printf("\n");

    return 0;
}
```


### 第3题

```c
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
```


### 第4题

```c
#include <stdio.h>
#include <stdlib.h>

#define N 10

int main()
{
    int a[10];

    /* 输入 */
    for (int i = 0; i < N; ++i)
    {
        scanf("%d", &a[i]);
    }

    /* 排序 */
    for (int left = 0; left <= N - 2; left++)
    {
        int min_id = left;
        for (int i = left + 1; i < N; i++)
        {
            if (a[i] < a[min_id])
            {
                min_id = i;
            }
        }
        int t     = a[left];
        a[left]   = a[min_id];
        a[min_id] = t;
    }

    /* 输出 */
    for (int i = 0; i < N; ++i)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
```


### 第5题

```c
#include <stdio.h>
#include <stdlib.h>

#define N 10

int main()
{
    int a[10];

    /* 输入 */
    for (int i = 0; i < N; ++i)
    {
        scanf("%d", &a[i]);
    }

    /* 排序 */
    for (int left = 0; left <= N - 2; left++)
    {
        int min_id = left;
        for (int i = left + 1; i < N; i++)
        {
            if (a[i] < a[min_id])
            {
                min_id = i;
            }
        }
        int t     = a[left];
        a[left]   = a[min_id];
        a[min_id] = t;
    }

    /* 输出 */
    for (int i = 0; i < N; ++i)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}```


### 第6题

```c
#include <stdio.h>
```
