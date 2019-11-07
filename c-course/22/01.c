


#include <stdio.h>


int main()
{
	int a;
	int *pa;

	printf("a = %d\n", a);
	printf("%p\n", pa);
	pa = &a;
	printf("%p\n", pa);
	scanf("%d", &a);
	return 0;
}

