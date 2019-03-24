#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define MAXN 5050

char tmp[MAXN];

char *input()
{
    int i;
    char *ans = (char *)malloc(sizeof(char) * MAXN);
    for (i = 0; i < MAXN; ++i) ans[i] = '\0';
    strcpy(tmp, "");
    while (strcmp(tmp, "START") != 0)
        gets(tmp);
    while (gets(tmp)) {
        if (strcmp(tmp, "END") == 0) break;
        if (strlen(tmp) != 0) strcat(ans, tmp);
        strcat(ans, "\n");
    }
    return ans;
}

char *beautify(char *str) {
    int i ;
    int anslen;
    anslen = 0;
    char *ans = (char *)malloc(sizeof(char) * MAXN);
    for (i = 0; i < strlen(str); ++i) {
        if (str[i] != ' ' && str[i] != '\t' && str[i] != '\n') {
            ans[anslen] = str[i];
            ++anslen;
        }
    }
    ans[anslen] = '\0';
    return ans;
}


int main(int argc, char *argv[]) {
    int t;
    scanf("%d", &t);
    while (t--) {
        char *a = input();
        char *b = input();
        if (strcmp(a, b) == 0) {
            printf("Accepted\n");
        }else if ( strcmp(beautify(a), beautify(b) ) == 0) {
            printf("Presentation Error\n");
        }else{
            printf("Wrong Answer\n");
        }
    }
    return 0;
}