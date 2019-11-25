## 实训八实训题目参考代码





### 第1题

定义一个结构体类型，包括职工的如下信息:职工号、姓名、年龄、工 资和职称，输入 3 个人的信息，然后输出。 


```c
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

```
### 第2题

编程实现静态链表的建立和输出。 


```c
#include <stdio.h>
#include <stdlib.h>

struct SqList {
    int *data;
    int size;
};

void sqlist_create(struct SqList *sq_list, int size) {
    sq_list->size = size;
    sq_list->data = (int *) malloc(size * sizeof(int));
}

void sqlist_destory(struct SqList *sq_list) {
    free(sq_list->data);
    sq_list->data = NULL;
    sq_list->size = 0;
}

void sqlist_show(struct SqList *sq_list) {
    printf("[");
    for (int i = 0; i < sq_list->size; i++) {
        if (i != 0) {
            printf(" ");
        }
        printf("%d", sq_list->data[i]);
    }
    printf("]");
    printf("\n");
}

int main() {
    struct SqList list;
    sqlist_create(&list, 10);
    sqlist_show(&list);
    sqlist_destory(&list);
    return 0;
}
```


