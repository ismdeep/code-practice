#include <stdio.h>
#include <string.h>

struct Date
{
	int year;
	int month;
	int day;
};

struct Student
{
	char id[100]; /* 学号 */
	char name[100]; /* 姓名 */
	char sex; /* f:Female m:Male */
	struct Date birth_date; /* 出生年月日 */
};

int main()
{
	struct Student students[100];
	return 0;
}
