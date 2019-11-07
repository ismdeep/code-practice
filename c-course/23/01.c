#include <stdio.h>

int sum (int n)
{
    if (0 == n)
    {
        return 0;
    }
    int ans = n + sum(n - 1);
    return ans;
}

int main() {
    printf("%d\n", sum(5));
    return 0;
}
