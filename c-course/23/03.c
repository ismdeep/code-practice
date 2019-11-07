#include <stdio.h>
#include <stdbool.h>



bool is_prime(int n)
{
	if (n <= 1)
	{
		return false;
	}

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
	for (int val = 0; val <= 1000; val++)
	{
		if (is_prime(val))
		{
			printf("%d ", val);
		}
	}
	printf("\n");
	return 0;
}
