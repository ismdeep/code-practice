#include <stdio.h>
#include <stdlib.h>

int main()
{
	int sum, n, a;
	scanf("%d", &n);
	sum = 0;
	a = 1;
	while (a <= n)
	{
		sum += a;
		a++;
	}
	printf("sum = %d\n", sum);
	return 0;
}

