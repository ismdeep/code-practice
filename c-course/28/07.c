


#include <stdio.h>

struct Date
{
	int year;
	int month;
	int day;
};


struct Student
{
	char ID[20]; /* 身份证号码 */
	char student_id[20]; /* 学号 */
	char name[50];
	char phone[20];
	char sex; /* f:女性 m:男性 */
	struct Date birth_date;
};

int main()
{
	struct Student stu;
	struct Student *p_stu;
	p_stu = &stu;
	strcpy(stu.ID, "20190002");
	strcpy(p_stu->name, "Del Cooper");

	stu.birth_date.year  = 1998;
	stu.birth_date.month = 11;
	stu.birth_date.day   = 11;

	p_stu->birth_date.year = 1998;
	(*p_stu).birth_date.year = 1998;

	printf("%s\n", stu.ID);
	printf("%s\n", p_stu->ID);


	struct Student students[100];
	struct Student *stus = malloc(100 * sizeof(struct Student));





	return 0;
}

