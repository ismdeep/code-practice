#include <stdio.h>
#include <stdlib.h>

int main()
{
	int line, item;
	for (line = 1; line <= 9; line++)
	{
		for (item = 1; item <= line; item++)
		{
			if (1 == item)
			{
				printf("%d*%d=%d ", item, line, item * line);
			}
			else
			{
				printf("%d*%d=%2d ", item, line, item * line);
			}
		}
		printf("\n");
	}
	return 0;
}
