#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main()
{
	srand(time(NULL));
	printf("%d\n", rand() % 100);
	return 0;
}

