/*
Usage: gendata [min=1] [max=100] [seed=1] [count=10] [output-count=1]
Default:
	min=1
	max=10
	seed=-1
	count=10
	output-count=1
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int str_find(char *str, char *p)
{
	printf("str={%s}\np={%s}\n", str, p);
	int len_str = strlen(str);
	int len_p   = strlen(p);
	for(int i = 0; i <= len_str - len_p; i++)
	{
		bool found = true;
		for (int j = 0; found && j < len_p; j++)
		{
			if (str[i+j] != p[j])
			{
				found = false;
			}
		}
		if (found)
		{
			return i;
		}
	}
	return -1;
}

char **split(char *str)
{
	printf("%s\n", str);
	printf("%d\n", str_find(str, "="));
}

char *parse_args(int argc, const char *argv[], const *key)
{
}

int main(int argc, const char *argv[])
{
	// printf("%s\n", parse_args(argc, argv, "min"));
	split("min=1");
	return 0;
}

