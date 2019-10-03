#include <iostream>
#include <cstdio>

using namespace std;

void swap (int* a, int* b) {
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

void sort_abc(int* a, int* b, int* c) {
    if (*a > *b) swap(a, b);
    if (*a > *c) swap(a, c);
    if (*b > *c) swap(b, c);
}


int main() {
#ifdef ISMDEEP_LOCAL
    freopen("in.txt", "r", stdin);
#endif
    int t;
    scanf("%d", &t);
    while (t--) {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        sort_abc(&a, &b, &c);
        if (a * a + b * b == c * c) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
