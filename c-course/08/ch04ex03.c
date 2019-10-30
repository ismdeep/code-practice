#include <stdio.h>

int main() {
	float r, c, area; /* r半径 c周长 area面积 */
	scanf("%f", &r);

	c    = 2 * 3.141592653 * r; /* 计算周长 */
	area = 3.141592653 * r * r; /* 计算面积 */

	printf("周长：%f\n", c);
	printf("面积：%f\n", area);

	return 0;
}