//
// Created by ismdeep on 2019-03-21.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define INC_SIZE 1024


struct SqList {
    int *elem;
    size_t length;
    size_t listsize;
};


void sqlist_init(struct SqList *sqlist, size_t listsize) {
    sqlist->elem = malloc(sizeof(int) * listsize);
    sqlist->length = 0;
    sqlist->listsize = listsize;
}

bool sqlist_full(struct SqList *sqlist) {
    return sqlist->length >= sqlist->listsize;
}

void sqlist_append(struct SqList *sqlist, int val) {
    if (sqlist_full(sqlist)) {
        int *arr = malloc(sizeof(int) * (sqlist->length));
        for (size_t i = 0; i < sqlist->length; ++i) {
            arr[i] = sqlist->elem[i];
        }
        free(sqlist->elem);
        sqlist->elem = malloc(sizeof(int) * (sqlist->listsize + INC_SIZE));
        for (size_t i = 0; i < sqlist->length; ++i) {
            sqlist->elem[i] = arr[i];
        }
        free(arr);
        sqlist->listsize = sqlist->listsize + INC_SIZE;
    }
    sqlist->elem[sqlist->length] = val;
    ++sqlist->length;
}

void sqlist_insert(struct SqList *sqlist, int val) {

}

int main(int argc, char *argv[]) {
    struct SqList list;
    sqlist_init(&list, 10);
    printf("sqlist_full => %d\n", sqlist_full(&list));
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);
    sqlist_append(&list, 1);

    return 0;
}