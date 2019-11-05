#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char *str;
	str = malloc(100 * sizeof(char));
	strcpy(str, "hello");
	printf("%s\n", str);
	printf("%lu\n", strlen(str));

	return 0;
}

