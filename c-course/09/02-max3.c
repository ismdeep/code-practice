#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a, b, c, m;
	scanf("%d%d%d", &a, &b, &c);
	if (a > b)
	{
		m = a;
	}
	else
	{
		m = b;
	}

	if (m > c)
	{
		m = m;
	}
	else
	{
		m = c;
	}

	printf("%d\n", m);

	return 0;
}
