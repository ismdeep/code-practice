
#include <stdio.h>

void swap(int *a, int *b)
{
	int t;
	t = *a;
	*a = *b;
	*b = t;
}


int main()
{
	int a, b;
	a = 1;
	b = 2;

	swap(&a, &b);

	return 0;
}

