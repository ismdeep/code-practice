#include <stdio.h>
#include <stdlib.h>

int max(int a, int b)
{
	int m;
	if (a > b)
	{
		m = a;
	}
	else
	{
		m = b;
	}
	return m;
}

int max3(int a, int b, int c)
{
	int m;
	m = max(a, b);
	m = max(m, c);
	return m;
}

int main()
{
	int a, b, c, max_value;
	scanf("%d%d%d", &a, &b, &c);
	printf("%d %d %d\n", a, b, c);

	max_value = max3(a, b, c);

	printf("max_value = %d\n", max_value);

	return 0;
}
