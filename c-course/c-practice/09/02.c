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