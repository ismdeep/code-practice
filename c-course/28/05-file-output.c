


#include <stdio.h>

int main()
{
	FILE *fp;
	/* 1. 打开文件 */
	fp = fopen("out.txt", "a");

	/* 2. 写入数据 */
	fprintf(fp, "%d\n", 333);

	/* 3. 关闭文件 */
	fclose(fp);
	return 0;
}

