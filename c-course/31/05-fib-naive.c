


#include <stdio.h>

unsigned long long fib(int n)
{
	if (n <= 2)
	{
		return 1;
	}

	return fib(n-1) + fib(n-2);
}


int main()
{
	int n;
	scanf("%d", &n);
	printf("%llu\n", fib(n));
	return 0;
}
