




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
	printf("a:%d   b:%d\n", a, b);
	swap(&a, &b);
	printf("a:%d   b:%d\n", a, b);
	return 0;
}
