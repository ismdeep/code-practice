#include <stdio.h>

int main() {
	int no;      /* 小明的学号 */
	float score; /* 小明的成绩 */

	printf("请输入小明的学号：");
	scanf("%d", &no);

	printf("请输入小明的成绩：");
	scanf("%f", &score);

	printf("小明同学的学号是%d，成绩是%.1f\n", no, score);
	return 0;
}