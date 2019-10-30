#include <stdio.h>
#include <stdlib.h>

int main()
{
	int sum, n, a;
	scanf("%d", &n);
	sum = 0;
	a = 1;
	do{
		sum += a;
		a++;
	}while (a <= n);
	printf("sum = %d\n", sum);
	return 0;
}

