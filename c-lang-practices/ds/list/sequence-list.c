//
// Created by ismdeep on 2019-03-21.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

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


int main(int argc, char *argv[]) {

    return 0;
}