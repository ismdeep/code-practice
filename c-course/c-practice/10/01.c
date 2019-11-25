#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE 1024

int main(int argc, char const *argv[]) {
    FILE *fp_read = fopen(argv[1], "rb");
    if (NULL == fp_read) {
        printf("can not open [%s].\n", argv[1]);
        return -1;
    }

    FILE *fp_write = fopen(argv[2], "wb");
    if (NULL == fp_write) {
        printf("can not open [%s].\n", argv[2]);
        return -1;
    }

    char buff[BUF_SIZE];
    int n;
    while ((n = fread(buff, 1, BUF_SIZE, fp_read)) > 0) {
        fwrite(buff, n, 1, fp_write);
    }

    fclose(fp_read);
    fclose(fp_write);

    return 0;
}
