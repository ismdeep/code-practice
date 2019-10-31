#include <stdio.h>

int main()
{
    char str[100];
    gets(str); /* 通过 gets() 函数读取整行字符串，注意区别gets和scanf输入的区别。 */
    puts(str); /* 通过 puts() 函数输出字符串 */
    return 0;
}
