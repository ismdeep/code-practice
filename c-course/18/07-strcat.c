#include <stdio.h>
#include <string.h>

int main()
{
    char str1[100] = "hello";
    char str2[100] = "heal";
    printf("%s\n", strcat(str1, str2));
    return 0;
}