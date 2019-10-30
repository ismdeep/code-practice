#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
	int v, i;
	bool is_prime;
	
	for (v = 2; v <= 1000; v++)
	{
		is_prime = true;
		for (i = 2; i < v; i++)
		{
			if (v % i == 0)
			{
				is_prime = false;
				break;
			}
		}
	
		if (!is_prime)
		{
			continue;
		}
		printf("%d ", v);
	}
	printf("\n");

	return 0;
}

