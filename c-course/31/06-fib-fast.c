


#include <stdio.h>
#include <stdlib.h>

unsigned long long fib(int n)
{
	unsigned long long *a;
	a = malloc((n + 1) * sizeof(unsigned long long));
	a[1] = 1;
	a[2] = 1;
	for (int i = 3; i <= n; i++)
	{
		a[i] = a[i-1] + a[i-2];
	}
	return a[n];
}


int main()
{
	int n;
	scanf("%d", &n);
	printf("%llu\n", fib(n));
	return 0;
}
