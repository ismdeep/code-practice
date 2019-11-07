#include <stdio.h>






int main()
{
	int a[10];
	for (int i = 0; i < 10; i++)
	{
		a[i] = i * i;
	}

	printf("a     => %p\n", a);
	for (int i = 0; i < 10; i++)
	{
		printf("&a[%d] => %p\n", i, &a[i]);
	}
	return 0;
}

