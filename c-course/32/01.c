



#include <stdio.h>
#include <stdlib.h>

/*
     8  3 7 9 6 5 1 2
1 => 1* 3 7 9 6 5 8 2
2 => 1* 2* 7 9 6 5 8 3 
3 => 1* 2* 3 9 6 5 8 7
4 => 1* 2* 3 5 6 9 8 7

 */


void sort(int *a, int n)
{
	for (int left = 0; left <= n - 2; left++)
	{
		for (int i = left + 1; i < n; i++)
		{
			if (a[i] < a[left])
			{
				int t;
				t = a[left];
				a[left] = a[i];
				a[i] = t;
			}
		}
	}
}


int main()
{
	int n;
	int *data;

	/* 1. 输入 */
	scanf("%d", &n);
	data = malloc(n * sizeof(int));
	for (int i = 0; i < n; i++)
	{
		scanf("%d", data + i);
	}
	/* 2. 排序 */
	sort(data, n);
	/* 3. 输出 */
	for (int i = 0; i < n; i++)
	{
		printf("%d ", data[i]);
	}
	printf("\n");
	return 0;
}

