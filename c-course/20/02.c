

#include <stdio.h>







int sum(int n)
{
	if (1 == n)
	{
		return 1;
	}
	return sum(n - 1) + n;
}

int main()
{
	int n, val;
	scanf("%d", &n);
	val = sum(n);
	printf("%d\n", sum(n));
	return 0;
}

