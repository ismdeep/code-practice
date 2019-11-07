#include <stdio.h>
#include <string.h>


int main()
{
	char s1[10];
	char s2[10];

	printf("s1 @%p\n", s1);
	printf("s2 @%p\n", s2);
	gets(s2);
	printf("s1: %s\n", s1);
	printf("s2: %s\n", s2);
	return 0;
}
