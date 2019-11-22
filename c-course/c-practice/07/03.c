#include <stdio.h>
#include <stdlib.h>

int max_in_arr(int *a, int n)
{
	int max_val = a[0];
	for (int i = 1; i < n; i++)
	{
		if (a[i] > max_val)
		{
			max_val = a[i];
		}
	}
	return max_val;
}

int main()
{
	int n;
	int *a;
	scanf("%d", &n);
	a = malloc(n * sizeof(int));
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}
	printf("最大数字为：%d\n", max_in_arr(a, n));
	return 0;
}


