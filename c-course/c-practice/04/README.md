## 实训四实训题目参考代码

1. 任意输入两个整数，求它们的最大公约数。

    ```c
    #include <stdio.h>
    
    /* gcd => Greatest Common Divisor; 最大公约数 */
    int gcd(int a, int b)
    {
        int t;
        while (b)
        {
            t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
    
    int main()
    {
        int a, b;
        scanf("%d%d", &a, &b);
        printf("%d\n", gcd(a, b));
        return 0;
    }
    ```
    

    
2. 打印形状为直角三角形的乘法口诀。

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    
    int main()
    {
    	int line, item;
    	for (line = 1; line <= 9; line++)
    	{
    		for (item = 1; item <= line; item++)
    		{
    			if (1 == item)
    			{
    				printf("%d*%d=%d ", item, line, item * line);
    			}
    			else
    			{
    				printf("%d*%d=%2d ", item, line, item * line);
    			}
    		}
    		printf("\n");
    	}
    	return 0;
    }
    ```

    

3. 输入一个包含有三个数字字符的字符串，把该字符串转换为整型数据输出。（如：输入字符串123，则输出整形数据123）

    ```c
    #include <stdio.h>
    
    int main()
    {
        char str[10];
        int val;
    
        scanf("%s", str);
        val = (str[0] - '0') * 100 + (str[1] - '0') * 10 + (str[2] - '0');
    
        printf("%d\n", val);
        return 0;
    }
    ```

    

