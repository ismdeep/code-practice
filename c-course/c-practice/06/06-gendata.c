#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main()
{
    srand(time(NULL));
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("%d ", rand() % 100);
        }
        printf("\n");
    }
    
    return 0;
}
