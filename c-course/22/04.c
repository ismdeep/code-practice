
#include <stdio.h>


int main()
{
	int a;
	int *p;
	a = 2;
	p = &a;
	printf("%d\n", *p);
	printf("&a: %p\n", &a);
	printf(" p: %p\n",  p);
	printf("&p: %p\n", &p);

	return 0;
}

