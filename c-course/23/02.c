#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n)
{
	bool flag = true;
	for (int i = 2; i < n; i++)
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
	int val;
	scanf("%d", &val);
	if (is_prime(val))
	{
		printf("%d is a prime.\n", val);
	}
	else
	{
		printf("%d is not a prime.\n", val);
	}
	return 0;
}
