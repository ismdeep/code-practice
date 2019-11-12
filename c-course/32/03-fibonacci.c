#include <stdio.h>
#include <stdlib.h>


int fib(int n)
{
	return n <= 2 ? 1 : fib(n-1) + fib(n-2);
}

int main()
{
	int n;
	scanf("%d", &n);
	printf("%d\n", fib(n));
	return 0;
}

