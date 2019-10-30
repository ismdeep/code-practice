#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, a, sum;
	scanf("%d", &n);
	sum = 0;
	for (a = 1; a <= n; a++)
	{
		sum += a;
	}
	printf("sum = %d\n", sum);
	return 0;
}
