

/*
   n 个数找最大值
 */

#include <stdio.h>

int max(int a[], int n)
{
	if (1 == n)
	{
		return a[0];
	}
	int max_value;
	max_value = max(a, n - 1);
	if (max_value > a[n-1])
	{
		return max_value;
	}
	else
	{
		return a[n-1];
	}
}

int main()
{
	int a[10] = {1,3,5,5,3,6,34,56,23,89};
	int max_value;
	max_value = max(a, 10);
	return 0;
}

