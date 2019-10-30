#include <stdio.h>

int main() {
	char ch;
	scanf("%c", &ch);
	ch += 32; /* 将大写字母增加32即得到对应的小写字母。 */
	printf("%c\n", ch);
	return 0;
}
