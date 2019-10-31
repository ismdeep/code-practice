#include <stdio.h>

int main()
{
    int a[3][4] = {
        {2,4,2,3},
        {45,34,56,23},
        {3,2,2,3}
    };
    int mi, mj, i, j;

    mi = 0;
    mj = 0;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            if (a[i][j] > a[mi][mj])
            {
                mi = i;
                mj = j;
            }
        }
    }
    printf("a[%d][%d] = %d \n", mi, mj, a[mi][mj]);
    return 0;
}