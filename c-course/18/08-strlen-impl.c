#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    gets(str);
    int i, len;
    i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    len = i;
    printf("str len: %d\n", len);
    return 0;
}
