#include <stdio.h>

int main() {
    printf("%d\n", sizeof(float));
    float a = 78.00000000;
    float b = 76.40000000;
    float c = a - b;

    u_int32_t *pa = &a;
    u_int32_t *pb = &b;
    u_int32_t *pc = &c;
    printf("%x\n", *pa);
    printf("%x\n", *pb);
    printf("%x\n", *pc);


    printf("%f\n", c);
    return 0;
}
