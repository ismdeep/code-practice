#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
	int n, i;
	bool is_prime;

	scanf("%d", &n);
	is_prime = true;
	for (i = 2; i < n; i++)
	{
		if (n % i == 0)
		{
			is_prime = false;
			break;
		}
	}

	if (is_prime)
	{
		printf("%d is a prime.\n", n);
	}
	else
	{
		printf("%d is not a prime.\n", n);
	}
	return 0;
}

