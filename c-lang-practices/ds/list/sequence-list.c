//
// Created by ismdeep on 2019-03-21.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define INC_SIZE 5


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

void sqlist_expand_mem(struct SqList *sqlist) {
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

void sqlist_append(struct SqList *sqlist, int val) {
    if (sqlist_full(sqlist)) {
        sqlist_expand_mem(sqlist);
    }
    sqlist->elem[sqlist->length] = val;
    ++sqlist->length;
}



void sqlist_remove_by_index(struct SqList *sqlist, size_t _index_) {
    if (_index_ >= sqlist->length) return;
    for (size_t i = _index_ + 1; i < sqlist->length; ++i) {
        sqlist->elem[i - 1] = sqlist->elem[i];
    }
    --sqlist->length;
}


void sqlist_remove_by_value(struct SqList *sqlist, int val) {
    for (size_t i = sqlist->length; i > 0; --i) {
        if (sqlist->elem[i - 1] == val) {
            sqlist_remove_by_index(sqlist, i - 1);
        }
    }
}


void sqlist_insert(struct SqList *sqlist, size_t _index_, int val) {
    if (sqlist_full(sqlist)) {
        sqlist_expand_mem(sqlist);
    }
    if (_index_ >= sqlist->length) {
        sqlist_append(sqlist, val);
        return;
    }
    for (size_t i = sqlist->length; i > _index_; --i) {
        sqlist->elem[i] = sqlist->elem[i - 1];
    }
    sqlist->elem[_index_] = val;
    ++sqlist->length;
}


void sqlist_print(struct SqList *sqlist) {
    printf("sqlist @ %p", sqlist);
    printf(" sqlist->listsize: {%lu}", sqlist->listsize);
    printf(" sqlist->length: {%lu}  ", sqlist->length);
    for (size_t i = 0; i < sqlist->length; ++i) {
        printf("%d ", sqlist->elem[i]);
    }
    printf("\n");
}

void sqlist_destroy(struct SqList *sqlist) {
    free(sqlist->elem);
    sqlist->elem = NULL;
    sqlist->length = 0;
    sqlist->listsize = 0;
//    free(sqlist);
}


int main(int argc, char *argv[]) {
    struct SqList list;
    sqlist_init(&list, 5);
    printf("sqlist_full => %d\n", sqlist_full(&list));
    sqlist_append(&list, 1);
    sqlist_print(&list);
    sqlist_append(&list, 5);
    sqlist_print(&list);
    sqlist_append(&list, 0);
    sqlist_print(&list);
    sqlist_append(&list, 8);
    sqlist_print(&list);
    sqlist_append(&list, 3);
    sqlist_append(&list, 7);
    sqlist_append(&list, 9);
    sqlist_append(&list, 6);
    sqlist_append(&list, 5);
    sqlist_append(&list, 1);
    sqlist_append(&list, 2);
    sqlist_print(&list);
    sqlist_remove_by_value(&list, 1);
    sqlist_print(&list);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_insert(&list, 1, 2);
    sqlist_print(&list);
    sqlist_destroy(&list);
    sqlist_append(&list, 1);
    sqlist_print(&list);
    return 0;
}