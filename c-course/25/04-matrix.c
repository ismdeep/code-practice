#include <stdio.h>



int main()
{
	int **a;
	int n, m;
	n = 2;
	m = 3;
	a = malloc(n * sizeof(int*));
	for (int i = 0; i < n; i++)
	{
		a[i] = malloc(m * sizeof(int));
	}
	return 0;
}

