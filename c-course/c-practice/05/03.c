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