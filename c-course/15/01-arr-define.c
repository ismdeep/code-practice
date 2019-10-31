#include <stdio.h>

int main()
{
    int a[10]; /* 声明一个大小为10、元素类型为int的数组a */
    int c;
    c = a[0]; // 取出a数组中下标为0的元素的值
    a[0] = 1; // 给a数组中希彪为0的元素赋值
    printf("%d\n", a[0]);
    return 0;
}
