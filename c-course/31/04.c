/*
 2 + 22 + 222 + ....
 */

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;
	int sum;
	int a[10];


	/* 1. 对 a 进行初始化*/
	a[0] = 0;
	for (int i = 1; i < 10; i++)
	{
		a[i] = a[i-1] * 10 + 2;
	}

	/* 2. 累加 */	
	sum = 0;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
	{
		sum += a[i];
	}

	/* 3. 输出 sum */
	printf("%d\n", sum);
	return 0;
}

