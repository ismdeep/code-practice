




#include <stdio.h>


void swap(int *a, int *b)
{
	int t;
	t = *a;
	*a = *b;
	*b = t;
}

void sort(int *pa, int *pb, int *pc)
{
	if(*pa < *pb) swap(pa, pb);
	if(*pa < *pc) swap(pa, pc);
	if(*pb < *pc) swap(pb, pc);
}

int main()
{
	int a, b, c;
	a = 4;
	b = 2;
	c = 3;
	printf("a:%d   b:%d  c:%d\n", a, b, c);
	sort(&a, &b, &c);
	printf("a:%d   b:%d  c:%d\n", a, b, c);
	return 0;
}
