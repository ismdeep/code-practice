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