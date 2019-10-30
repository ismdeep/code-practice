#include <stdio.h>
#include <stdlib.h>

void swap(int x, int y)
{
	printf("x = %d    y = %d\n", x, y);
	int t;
	t = x;
	x = y;
	y = t;
	printf("x = %d    y = %d\n", x, y);
}

int main()
{
	int a, b;
	a = 2;
	b = 3;
	printf("a = %d    b = %d\n", a, b);
	swap(a, b);
	printf("a = %d    b = %d\n", a, b);
	return 0;
}
