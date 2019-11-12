


#include <stdio.h>

int main()
{
	int a[10];
	int n, sum;

	/* 1. 预先处理a */
	a[0] = 0;
	for (int i = 1; i <= 9; i++)
	{
		a[i]= a[i-1] * 10 + 2;
	}

	/* 2. 输入n */
	scanf("%d", &n);

	/* 3. 计算累加 */
	sum = 0;
	for (int i = 1; i <= n; i++)
	{
		sum += a[i];
	}

	/* 4. 输出 */
	printf("%d\n", sum);
	return 0;
}

