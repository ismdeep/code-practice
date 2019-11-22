## 实训五实训题目参考代码




### 第1题

任意输入一行字符，分别统计字母、数字、空格和其它字符的个数。

```c
/*
任意输入一行字符，分别统计字母、数字、空格和其它字符的个数。
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool is_alphabet(char ch)
{
    return ('a' <= ch && ch <= 'z') || ('A' <= ch && ch <= 'Z');
}

bool is_digital(char ch)
{
    return '0' <= ch && ch <= '9';
}

bool is_space(char ch)
{
    return ' ' == ch;
}

int main()
{
    char str[65535];
    int alphabet, digital, space, other;

    gets(str);
    
    alphabet = 0;
    digital  = 0;
    space    = 0;
    other    = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        if (is_alphabet(str[i]))
        {
            ++alphabet;
        }
        else if (is_digital(str[i]))
        {
            ++digital;
        }
        else if (is_space(str[i]))
        {
            ++space;
        }
        else
        {
            ++other;
        }
    }
    printf("字母个数：%d\n", alphabet);
    printf("数字个数：%d\n", digital);
    printf("空格个数：%d\n", space);
    printf("其他个数：%d\n", other);
    return 0;
}

```
### 第2题

打印1000 之内的所有完数。一个数如果正好等于它的因子之和，这个数就称之为完数。

```c
#include <stdio.h>
#include <stdbool.h>

bool is_perfect_number(int n)
{
    int sum = 0;
    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }
    return sum == n;
}


int main()
{
    for (int val = 1; val <= 1000; val++)
    {
        if(is_perfect_number(val))
        {
            printf("%d\n", val);
        }
    }
    return 0;
}

```
### 第3题

实现菜单功能，当输入为“退出”的控制时结束。

```
*************************************
* 1---input                         *
* 2---search                        *
* 3---sort                          *
* 4---delete                        *
* 0---exit                          *
*************************************
please input your choice(0---4)：
```

```c
#include <stdio.h>

void menu_help()
{
    printf("*************************************\n");
    printf("* 1---input                         *\n");
    printf("* 2---search                        *\n");
    printf("* 3---sort                          *\n");
    printf("* 4---delete                        *\n");
    printf("* 0---exit                          *\n");
    printf("*************************************\n");
    printf("please input your choice(0---4)：");
}

int main()
{
	int choose;
	
	while (menu_help(), scanf("%d", &choose), choose)
	{
		switch(choose)
		{
			case 1:
				printf("Input\n");
				break;
			case 2:
				printf("Search\n");
				break;
			case 3:
				printf("Sort\n");
				break;
			case 4:
				printf("Delete\n");
				break;
		}
	}
	return 0;
}
```
### 第4题

编程实现10 道 `+` 、 `-` 、 `*` 、 `/` 的运算。

```c
#include <stdio.h>
#include <stdlib.h>

#define TIMES(id, size) for(int id = 0; id < (size); id++)

void welcome_msg()
{
    printf("calculator 1.0.0\n");
    printf("Type Simple formula, e.g. 1 + 2\n");
}

int main()
{
    int a, b, ans;
    char op;
    welcome_msg();

    TIMES(time_id, 10)
    {
        printf(">>> ");
        scanf("%d %c %d",&a, &op, &b);
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
                printf("error\n");
                continue;
        }
        printf("%d\n", ans);
    }
    
    return 0;
}
```




