#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main()
{
    srand(time(NULL));
    for (int i = 0; i < 10; ++i)
    {
        printf("%d ", rand() % 100);
    }

    printf("\n%d\n", rand() % 100);

    return 0;
}
