#include <stdio.h>

int cnt;

void h(int n, char a, char b, char c) {
    if (n == 1) {
        printf("%d:%c->%c\n", ++cnt, a, c);
    }else{
        h(n - 1, a, c, b);
        printf("%d:%c->%c\n", ++cnt, a, c);
        h(n - 1, b, a, c);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    cnt = 0;
    h(n, 'A', 'B', 'C');
    return 0;
}