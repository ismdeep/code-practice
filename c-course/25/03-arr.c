#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;
	scanf("%d", &n);
	int *a;
    a = malloc( n * sizeof(int) );
	for (int i = 0; i < n; i++)
	{
		a[i] = i;
	}
	return 0;
}

