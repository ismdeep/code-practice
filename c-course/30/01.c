


#include <stdio.h>

#define MAXN 1000
#define TIMES(id, size) for(int id = 0; id < (size); id++)
#define ADD(i,j) (i) + (j)
#define MUL(i,j) (i) * (j)

int main()
{
	printf("%d\n", MUL(2,3+4) );
	return 0;
}
