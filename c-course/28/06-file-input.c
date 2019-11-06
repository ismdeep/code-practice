


#include <stdio.h>

int main()
{
	FILE *fp;
	int a;
	/* 1. 打开文件 */
	fp = fopen("out.txt", "r");

	/* 2. 写入数据 */
	fscanf(fp, "%d", &a);
	printf("The a input from file is %d\n", a);

	/* 3. 关闭文件 */
	fclose(fp);
	return 0;
}

