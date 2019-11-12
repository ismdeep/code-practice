#include <stdio.h>



int main()
{
	int a[2][3] = {
		{3,4,5},
		{1,3,5}
	};

	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			printf("(%d,%d) = %p\n",
					  i, j, &a[i][j]);
		}
	}

	int *p;
	int i;

	p = a;
	for (i = 0; i < 6; i++) 
	{
		printf("%p ", p);
		printf("%d\n", *p);
		++p;
	}

	return 0;
}
