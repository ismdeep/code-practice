#include <stdio.h>

void init(int *a, int n)
{
	for (int i = 0; i < n; i++)
	{
		a[i] = i * i;
	}
}

void print_arr(short int *a, int n)
{
	for (int i = 0; i < n; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
}

int main()
{
	int a[10];
	init(a, 10);
	print_arr(a, 10);
	return 0;
}
