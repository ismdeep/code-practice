#include <stdio.h>

int main()
{
    char str[10];
    int val;

    scanf("%s", str);
    val = (str[0] - '0') * 100 + (str[1] - '0') * 10 + (str[2] - '0');

    printf("%d\n", val);
    return 0;
}
