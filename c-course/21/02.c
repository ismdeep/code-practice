#include <stdio.h>


int global_val;

void change_val()
{
	int global_val;
	global_val = 12;
}


int main()
{
	global_val = 0;
	printf("global_val: %d\n", global_val);
	change_val();
	printf("global_val: %d\n", global_val);
	return 0;
}

