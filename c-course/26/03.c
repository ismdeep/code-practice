


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void set_hello(char *str)
{
	strcpy(str, "hello");
}

int main()
{
	char *s;
	s = malloc(100 * sizeof(char));
	set_hello(s);
	printf("%s\n", s);
	return 0;
}

