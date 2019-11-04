



#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, i;
	int *pa;

	scanf("%d", &n);
	printf("n = %d\n", n);
	pa = malloc(n * sizeof(int));
	printf("%p\n", pa);

	scanf("%d", &n);



	for (i = 0; i < n; i++)
	{
		pa[i] = i;
	}

	for (i = 0; i < n; i++)
	{
		printf("%d ", pa[i]);
	}

	printf("\n");


	return 0;
}

