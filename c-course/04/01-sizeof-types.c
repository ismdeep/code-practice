#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("short int size: %d\n",
           sizeof(short int) * 8);
    printf("int size:%d\n",
           sizeof(int) * 8);
    printf("long size:%d\n",
           sizeof(long) * 8);
    printf("long long size:%d\n",
           sizeof(long long) * 8);
    return 0;
}
