#include <stdio.h>

/* gcd => Greatest Common Divisor; 最大公约数 */
int gcd(int a, int b)
{
	int t;
	while (b)
	{
		t = a % b;
		a = b;
		b = t;
	}
	return a;
}

int main()
{
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", gcd(a, b));
	return 0;
}
