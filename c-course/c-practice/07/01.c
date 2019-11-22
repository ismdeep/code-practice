#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define BOOL short int
#define TRUE 1
#define FALSE 0

/* 我觉得 fun_a 这个函数名没有意思，所有还是自己用 is_prime 这个函数名称吧。 */
BOOL is_prime(int val)
{
	if (val <= 1)
	{
		return FALSE;
	}

	int stop = sqrt(val);
	for (int i = 2; i <= stop; i++)
	{
		if (val % i == 0)
		{
			return FALSE;
		}
	}
	return TRUE;
}

int main()
{
	int n;
	scanf("%d", &n);
	if (is_prime(n))
	{
		printf("%d is a prime.\n", n);
	}
	else
	{
		printf("%d is not a prime.\n", n);
	}
	return 0;
}

