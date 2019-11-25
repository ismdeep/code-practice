#include <stdio.h>
#include <stdlib.h>

struct Staff {
    char id[50]; /* 职工号 */
    char name[50]; /* 姓名 */
    unsigned short int age; /* 年龄 */
    float salary; /* 工资 */
    char job_title[50]; /* 职称 */
};

int main() {
    int n = 3;
    while (n--) {
        struct Staff staff1;
        printf("请输入职工号：");
        scanf("%s", staff1.id);
        printf("请输入姓名：");
        scanf("%s", staff1.name);
        printf("请输入年龄：");
        scanf("%hu", &staff1.age);
        printf("请输入工资：");
        scanf("%f", &staff1.salary);
        printf("请输入职称：");
        scanf("%s", staff1.job_title);

        printf("-----------------------------\n");
        printf("     职工信息\n");
        printf("职工号： %s\n", staff1.id);
        printf("姓名： %s\n", staff1.name);
        printf("年龄： %u\n", staff1.age);
        printf("工资： %.2f\n", staff1.salary);
        printf("职称： %s\n", staff1.job_title);
        printf("-----------------------------\n");
    }
    return 0;
}
