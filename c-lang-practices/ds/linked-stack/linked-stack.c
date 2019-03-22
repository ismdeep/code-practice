//
// Created by ismdeep on 2019/3/19.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct StackNode {
    int val;
    struct StackNode *prev;
    struct StackNode *next;
};

struct Stack {
    size_t size;
    struct StackNode *head;
};

void stack_init(struct Stack *stack) {
    stack->head = malloc(sizeof(struct StackNode));
    stack->head->val = 0;
    stack->head->prev = NULL;
    stack->head->next = NULL;
    stack->size = 0;
}

void stack_push(struct Stack *stack, int val) {
    struct StackNode *cur;
    cur = stack->head;
    while (cur->next != NULL) {
        cur = cur->next;
    }
    struct StackNode *node;
    node = malloc(sizeof(struct StackNode));
    node->val = val;
    node->next = NULL;
    node->prev = cur;
    cur->next = node;
    ++stack->size;
}

bool stack_is_empty(struct Stack *stack) {
    if (0 == stack->size) {
        return true;
    }
    return false;
}

struct StackNode *stack_top(struct Stack *stack) {
    struct StackNode *cur;
    cur = stack->head;
    while (cur->next != NULL) {
        cur = cur->next;
    }
    return cur;
}

void stack_pop(struct Stack *stack) {
    struct StackNode *cur;
    cur = stack->head;
    while (cur->next != NULL) {
        cur = cur->next;
    }

    if (cur != stack->head) {
        cur->prev->next = NULL;
        cur->prev = NULL;
        free(cur);
        cur = NULL;
        --stack->size;
    }
}


size_t stack_size(struct Stack *stack) {
    return stack->size;
}


void stack_print(struct Stack *stack) {
    struct StackNode *cur;
    cur = stack->head;
    printf("stack @ %p : head", stack);
    while (cur->next != NULL) {
        printf("->{%d}", cur->next->val);
        cur = cur->next;
    }
    printf("\n");
}


int main(int argc, char *argv[]) {
    struct Stack stack1;
    stack_init(&stack1);
    stack_print(&stack1);
    stack_push(&stack1, 1);
    stack_print(&stack1);
    stack_print(&stack1);
    stack_push(&stack1, 2);
    stack_print(&stack1);
    stack_push(&stack1, 4);
    stack_print(&stack1);
    stack_push(&stack1, 3);
    stack_print(&stack1);
    stack_pop(&stack1);
    stack_print(&stack1);
    stack_pop(&stack1);
    stack_print(&stack1);
    stack_pop(&stack1);
    stack_print(&stack1);
    stack_pop(&stack1);
    stack_print(&stack1);
    stack_pop(&stack1);
    stack_print(&stack1);
    stack_pop(&stack1);
    stack_print(&stack1);
    return 0;
}