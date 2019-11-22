#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *my_strcat(const char *str1, const char *str2) {
    int len_str1 = strlen(str1);
    int len_str2 = strlen(str2);
    char *str = (char *) malloc((len_str1 + len_str2) * sizeof(char));
    memset(str, 0, (len_str1 + len_str2) + sizeof(char));
    for (int i = 0; i < len_str1; i++) {
        str[i] = str1[i];
    }
    for (int i = 0; i < len_str2; i++) {
        str[len_str1 + i] = str2[i];
    }
    return str;
}


int main(int argc, char const *argv[])
{
    printf("%s\n", my_strcat("hello", "world"));
    return 0;
}
