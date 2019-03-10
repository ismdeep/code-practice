#pragma comment(linker, "/STACK:102400000,102400000")
#include <stdio.h>
#include <stdlib.h>

struct Node{
    int val;
    struct Node *l, *r;
};


struct Node * init(struct Node *tree) {
    return nullptr;
}

void free_tree(struct Node *tree) {
    if (NULL == tree->l) {
        free_tree(tree->l);
    }
    if (NULL == tree->r) {
        free_tree(tree->r);
    }
    free(tree);
    tree = NULL;
}

struct Node * insert(struct Node *tree, int val) {
    if (nullptr == tree) {
        tree = (struct Node *) malloc(sizeof(struct Node));
        tree->val = val;
        tree->l = tree->r = nullptr;
        return tree;
    }

    if (tree->val > val) {
        /* go left */
        if (nullptr == tree->l) {
            struct Node *node = (struct Node *) malloc(sizeof(struct Node));
            node->val = val;
            node->l = node->r = nullptr;
            tree->l = node;
        }else{
            insert(tree->l, val);
        }
    }else{
        /* go right */
        if (nullptr == tree->r) {
            struct Node *node = (struct Node *) malloc(sizeof(struct Node));
            node->val = val;
            node->l = node->r = nullptr;
            tree->r = node;
        }else{
            insert(tree->r, val);
        }
    }
    return tree;
}


void output(struct Node *tree) {
    if (nullptr == tree) {
        return;
    }
    printf("%p {%6d} => l: %p    r: %p\n", tree, tree->val , tree->l, tree->r);
    output(tree->l);
    output(tree->r);
}

int main() {
    struct Node *tree = nullptr;
    printf("sizeof(struct Node): %lu\n", sizeof(struct Node));
    tree = init(tree);
    int a;
    for (int i = 0; i < 1000000; ++i) {
        tree = insert(tree, i);
    }
    output(tree);
    free_tree(tree);
    return 0;
}