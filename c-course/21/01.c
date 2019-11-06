





#include <stdio.h>
#include <stdbool.h>


bool is_prime(int n)
{
	if (n <= 1)
	{
		return false;
	}
	
	int i;
	for (i = 2; i <= n - 1; i++)
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
	int n;
	while (true)
	{
		scanf("%d", &n);
		if (is_prime(n))
		{
			printf("%d is a prime.\n", n);
		}
		else
		{
			printf("%d is not a prime.\n", n);
		}
	}
	return 0;
}

