#include <stdio.h>
#include <string.h>

struct Student
{
	char id[100]; /* 学号 */
	char name[100]; /* 姓名 */
	char sex; /* f:Female m:Male */
};

int main()
{
	struct Student student_info;
	strcpy(student_info.id, "20190023");
	strcpy(student_info.name, "Del Cooper");
	student_info.sex = 'm';
	printf("ID: %s\n", student_info.id);
	printf("Name: %s\n", student_info.name);
	printf("Sex: %c\n", student_info.sex);
	return 0;
}
