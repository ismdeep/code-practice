#include <stdio.h>

int main() {
	int num;
	int a, b, c; /* 分别用来存放num的个位、十位、百位数值 */
	int ans; /* 计算后的结果 */

	scanf("%d", &num);
	a = num % 10; /* 取出个位 */
	num /= 10;

	b = num % 10; /* 取出十位 */
	num /= 10;

	c = num;      /* 取出百位 */

	ans = a * 100 + b * 10 + c;

	printf("%d\n", ans);

	return 0;
}