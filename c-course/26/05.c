#include <stdio.h>
#include <stdlib.h>


void *create_array(int size, int sizeof_item)
{
	void *a = malloc(size * sizeof_item);
	return a;
}

void **create_matrix(int row, int col, int sizeof_item)
{
	void **a;
	a = malloc(row * col * sizeof_item);
}


int main()
{
	int *a;
	a = create_array(100, sizeof(int));

	double *d;
	d = create_array(200, sizeof(double));
}

