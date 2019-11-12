

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student
{
	char name[10];
	float score;
};


void sort(struct Student *a, int n)
{
	for (int left = 0; left <= n - 2; left++)
	{
		for (int i = left + 1; i < n; i++)
		{
			if (a[i].score < a[left].score)
			{
				struct Student t;
				strcpy(t.name, a[left].name);
				t.score = a[left].score;

				strcpy(a[left].name, a[i].name);
				a[left].score = a[i].score;

				strcpy(a[i].name, t.name);
				a[i].score = t.score;
			}
		}
	}
}


int main()
{
	int n;
	struct Student *data;

	/* 1. 输入 */
	scanf("%d", &n);
	data = malloc(n * sizeof(struct Student));
	for (int i = 0; i < n; i++)
	{
		scanf("%s %f", data[i].name, &data[i].score);
	}
	/* 2. 排序 */
	sort(data, n);
	/* 3. 输出 */
	printf("      Name |  Score\n");
	printf("-------------------\n");
	for (int i = 0; i < n; i++)
	{
		printf("%10s | %6.2f\n",
				data[i].name,
				data[i].score);
	}
	printf("\n");
	return 0;
}

