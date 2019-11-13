#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool is_upper(char ch)
{
	if ('A' <= ch && ch <= 'Z')
	{
		return true;
	}
	return false;
}


int main()
{
	char s[100];
	scanf("%s", s);
	for (int i = 0; i < strlen(s); i++)
	{
		if (is_upper(s[i]))
		{
			s[i] += 32;
		}
	}
	printf("%s\n", s);
	return 0;
}

