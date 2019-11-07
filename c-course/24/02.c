#include <stdio.h>


int main()
{
	int a[10];
	short int *p;

	for (int i = 0; i < 10; i++)
	{
		a[i] = i;
	}
	
	p = a;
	printf(" p => %p\n", p);
	printf("*p => %ld\n", *p);

	p++;	
	printf(" p => %p\n", p);
	printf("*p => %d\n", *p);

	p++;	
	printf(" p => %p\n", p);
	printf("*p => %d\n", *p);
	p++;	
	printf(" p => %p\n", p);
	printf("*p => %d\n", *p);
	p++;	
	printf(" p => %p\n", p);
	printf("*p => %d\n", *p);

	return 0;
}

