



#include <stdio.h>

void swap(int a, int b)
{
	int t;
	printf("swap() => a:%d    b:%d\n", a, b);
	t = a;
	a = b;
	b = t;
	printf("swap() => a:%d    b:%d\n", a, b);
}

int main()
{
	int a, b;
	a = 2;
	b = 4;
	printf("main() => a:%d    b:%d\n", a, b);
	swap(a, b);
	printf("main() => a:%d    b:%d\n", a, b);
	return 0;
}

