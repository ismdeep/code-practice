## 实训三实训题目参考代码

### 1

```c
#include <stdio.h>

void menu_help()
{
    printf("*************************************\n");
    printf("* 1---成绩输入                      *\n");
    printf("* 2---成绩插入                      *\n");
    printf("* 3---成绩查询                      *\n");
    printf("* 4---成绩排序                      *\n");
    printf("* 5---成绩删除                      *\n");
    printf("* 6---成绩输出                      *\n");
    printf("* 0---退出                          *\n");
    printf("*************************************\n");
}

int main()
{
    int choose;
    menu_help();
    while (printf("请输入你的选择(0---6): "), scanf("%d", &choose), choose)
    {
        if (1 == choose)
        {
            printf("您选择的是成绩输入\n");
        }
        else if (2 == choose)
        {
            printf("您选择的是成绩插入\n");
        }
        else if (3 == choose)
        {
            printf("您选择的是成绩查询\n");
        }
        else if (4 == choose)
        {
            printf("您选择的是成绩排序\n");
        }
        else if (5 == choose)
        {
            printf("您选择的是成绩删除\n");
        }
        else if (6 == choose)
        {
            printf("您选择的是成绩输出\n");
        }
        menu_help();
    }
    return 0;
}
```



### 2

```c
#include <stdio.h>

void swap(int *a, int *b)
{
    int t;
    t = *a;
    *a = *b;
    *b = t;
}

void arrange(int *a, int *b) {
    if (*a < *b) {
        swap(a, b);
    }
}

int main()
{
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    arrange(&a, &b);
    arrange(&a, &c);
    arrange(&b, &c);
    printf("%d %d %d\n", a, b, c);
    return 0;
}
```



### 3

```c
#include <stdio.h>

int main()
{
    int a, b, ans;
    char op;

    printf("请输入两个整数： ");
    scanf("%d%d", &a, &b);
    printf("请输入运算符（ + - * / ）： ");
    scanf(" %c", &op);

    if ('+' == op)
    {
        ans = a + b;
    }
    else if ('-' == op)
    {
        ans = a - b;
    }
    else if ('*' == op)
    {
        ans = a * b;
    }
    else if ('/' == op)
    {
        ans = a / b;
    }
    else
    {
        printf("请输入正确的运算符\n");
    }
    printf("%d %c %d = %d\n", a, op, b, ans);
    return 0;
}
```



### 4

```c
#include <stdio.h>

void menu_help()
{
	printf("*************************************\n");
	printf("* 1---成绩输入                      *\n");
	printf("* 2---成绩插入                      *\n");
	printf("* 3---成绩查询                      *\n");
	printf("* 4---成绩排序                      *\n");
	printf("* 5---成绩删除                      *\n");
	printf("* 6---成绩输出                      *\n");
	printf("* 0---退出                          *\n");
	printf("*************************************\n");
}

int main()
{
	int choose;
	menu_help();
	while (printf("请输入你的选择(0---6):  "), scanf("%d", &choose), choose)
	{
		switch(choose)
		{
			case 1:
				printf("您选择的是成绩输入\n");
				break;
			case 2:
				printf("您选择的是成绩插入\n");
				break;
			case 3:
				printf("您选择的是成绩查询\n");
				break;
			case 4:
				printf("您选择的是成绩排序\n");
				break;
			case 5:
				printf("您选择的是成绩删除\n");
				break;
			case 6:
				printf("您选择的是成绩输出\n");
				break;
		}
		menu_help();
	}
	return 0;
}
```



### 5

```c
#include <stdio.h>

int main()
{
    int a, b, ans;
    char op;

    printf("请输入两个整数： ");
    scanf("%d%d", &a, &b);
    printf("请输入运算符（ + - * / ）： ");
    scanf(" %c", &op);

    switch(op)
    {
        case '+':
            ans = a + b; break;
        case '-':
            ans = a - b; break;
        case '*':
            ans = a * b; break;
        case '/':
            ans = a / b; break;
        default:
            printf("请输入正确的运算符\n");
            return 0;
    }

    printf("%d %c %d = %d\n", a, op, b, ans);
    return 0;
}
```



### 6

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

int main()
{
    int target, val;

    srand(time(NULL));
    target = rand() % 100;
    do
    {
        printf("请输入数字： ");
        scanf("%d", &val);
        if (val == target)
        {
            printf("恭喜你！猜中了。\n");
            break;
        }
        if (val > target)
        {
            printf("嗨呀，猜大了。\n");
        }
        else
        {
            printf("嗨呀，猜小了。\n");
        }
    }while (true);
    
    return 0;
}
```

