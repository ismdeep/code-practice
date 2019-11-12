





#include <stdio.h>
#include <stdbool.h>

int main()
{
	char str[2000];
	bool is_pd;/* 是否是回文串 */

	/* 1. 输入字符串 */
	scanf("%s", str);

	/* 2. 判断是否是回文串 */
	is_pd = true;
	for (int i = 0; i < strlen(str) / 2; i++)
	{
		if(str[i] != str[strlen(str) - 1 - i])
		{
			is_pd = false;
		}
	}

	/* 3. 输出结果 */
	if (is_pd)
	{
		printf("%s is a palindromic string.\n", str);
	}
	else
	{
		printf("%s not is a palindromic string.\n", str);
	}

	return 0;
}

