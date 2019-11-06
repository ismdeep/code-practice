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
	struct Student student_info;
	strcpy(student_info.id, "20190023");
	strcpy(student_info.name, "Del Cooper");
	student_info.sex = 'm';

	student_info.birth_date.year  = 1985;
	student_info.birth_date.month = 11;
	student_info.birth_date.day   = 11;

	struct Student *p_stu;
	p_stu = &student_info;

	printf("ID: %s\n", (*p_stu).id);
	printf("ID: %s\n", p_stu->id);
	printf("Name: %s\n", p_stu->name);
	printf("Sex: %c\n", p_stu->sex);
	printf("Birth: %d-%d-%d\n",
			p_stu->birth_date.year,
			p_stu->birth_date.month,
			p_stu->birth_date.day
			);
	return 0;
}
