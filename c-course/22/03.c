



#include <stdio.h>

void swap(int *pa, int *pb)
{
	int t;
	printf("swap() =>  pa:%p     pb:%p\n", pa, pb);
	printf("swap() => *pa:%d    *pb:%d\n", *pa, *pb);
	t   = *pa;
	*pa = *pb;
	*pb = t;
	printf("swap() =>  pa:%p     pb:%p\n", pa, pb);
	printf("swap() => *pa:%d    *pb:%d\n", *pa, *pb);
}

int main()
{
	int a, b;
	a = 2;
	b = 4;
	printf("main() => &a:%p    &b:%p\n", &a, &b);
	printf("main() =>  a:%d     b:%d\n", a, b);
	swap(&a, &b);
	printf("main() => a:%d    b:%d\n", a, b);
	return 0;
}

