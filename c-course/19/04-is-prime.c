#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>


bool is_prime(int n)
{
	if (n <= 1)
	{
		return false;
	}

	int stop = sqrt(n);
	int i;
	for (i = 2; i <= stop; i++)
	{
		if (n % i == 0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int v;
	for (v = 2; v <= 1000; v++)
	{
		if (is_prime(v))
		{
			printf("%d ", v);
		}
	}
	printf("\n");
	return 0;
}
