


#include <stdio.h>
#include <stdlib.h>

void **create_matrix(int row, int col, int sizeof_item)
{
	int **a;
	a = malloc(n * sizeof(int *));
	for (i = 0; i < n; i++)
	{
		a[i] = malloc(m * sizeof(int));
	}
	return a;
}

int main()
{
	int **a;
	int n, i, j, m;
	n = 2;
	m = 3;
	a = create_matrix(n, m, sizeof(int));
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; ++j)
		{
			a[i][j] = i + j;
		}
	}

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; ++j)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}

	return 0;
}

