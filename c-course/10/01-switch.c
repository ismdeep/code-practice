#include <stdio.h>
#include <stdlib.h>

int main()
{
	char ch;
	printf("Input grade: ");
	scanf("%c", &ch);
	switch(ch)
	{
		case 'A':
			printf("Your score is in [90, 100].\n");
			break;
		case 'B':
			printf("Your score is in [80, 89].\n");
			break;
		case 'C':
			printf("Your score is in [70, 79].\n");
			break;
		case 'D':
			printf("Your score is in [60, 69].\n");
			break;
		case 'E':
			printf("Your score is in [0, 59].\n");
			break;
		default:
			printf("Please input the right grade.\n");
	}
	return 0;
}
