/*
任意输入一行字符，分别统计字母、数字、空格和其它字符的个数。
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool is_alphabet(char ch)
{
    return ('a' <= ch && ch <= 'z') || ('A' <= ch && ch <= 'Z');
}

bool is_digital(char ch)
{
    return '0' <= ch && ch <= '9';
}

bool is_space(char ch)
{
    return ' ' == ch;
}

int main()
{
    char str[65535];
    int alphabet, digital, space, other;

    gets(str);
    
    alphabet = 0;
    digital  = 0;
    space    = 0;
    other    = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if (is_alphabet(str[i]))
        {
            ++alphabet;
        }
        else if (is_digital(str[i]))
        {
            ++digital;
        }
        else if (is_space(str[i]))
        {
            ++space;
        }
        else
        {
            ++other;
        }
    }
    printf("字母个数：%d\n", alphabet);
    printf("数字个数：%d\n", digital);
    printf("空格个数：%d\n", space);
    printf("其他个数：%d\n", other);
    return 0;
}
