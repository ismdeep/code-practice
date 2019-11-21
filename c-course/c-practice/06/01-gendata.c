#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main()
{
    srand(time(NULL));
    for (int i = 0; i < 20; ++i)
    {
        printf("%d ", rand() % 100 - 50);
    }
    printf("\n");
    return 0;
}
