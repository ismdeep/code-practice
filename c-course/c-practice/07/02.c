#include <stdio.h>

void menu_help()
{
	printf("*****************************\n");
	printf("* 1---------加法            *\n");
	printf("* 2---------减法            *\n");
	printf("* 3---------乘法            *\n");
	printf("* 4---------除法            *\n");
	printf("* 0---------退出            *\n");
	printf("*****************************\n");
	printf("请输入你的选择（0 - 4）：");
}

void add()
{
	printf("请输入两个数字：");
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", a + b);
}

void sub()
{
	printf("请输入两个数字：");
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", a - b);
}

void mul()
{
	printf("请输入两个数字：");
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", a * b);
}

void div()
{
	printf("请输入两个数字：");
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", a / b);
}

int main()
{
	int choose;
	while(menu_help(), scanf("%d", &choose), choose)
	{
		switch(choose)
		{
			case 1:
				add(); break;
			case 2:
				sub(); break;
			case 3:
				mul(); break;
			case 4:
				div(); break;
			default:
				printf("请选择正确的选项。\n");
		}
	}
	return 0;
}

