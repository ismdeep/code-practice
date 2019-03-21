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
    struct StackNode *tail;
};

void stack_init(struct Stack *stack) {
    stack->head = malloc(sizeof(struct StackNode));
    stack->head->val = 0;
    stack->head->prev = NULL;
    stack->head->next = NULL;
    stack->tail = stack->head;
    stack->size = 0;
}

void stack_push(struct Stack *stack, int val) {
    struct StackNode *node;
    node = malloc(sizeof(struct StackNode));
    node->val = val;
    node->next = NULL;
    node->prev = stack->tail;
    stack->tail->next = node;
    stack->tail = node;
    ++stack->size;
}

bool stack_is_empty(struct Stack *stack) {
    if (0 == stack->size) {
        return true;
    }
    return false;
}

struct StackNode *stack_top(struct Stack *stack) {
    return stack->tail;
}

void stack_pop(struct Stack *stack) {
    if (stack->head == stack->tail) return;
    stack->tail->prev->next = NULL;
    stack->tail = stack->tail->prev;
    free(stack->tail->next);
    if (stack->size > 0) {
        --stack->size;
    }
}


size_t stack_size(struct Stack *stack) {
    return stack->size;
}


void stack_print(struct Stack *stack) {
    struct StackNode *cur;
    cur = stack->head;
    printf("stack(%lu) @ %p : head", stack->size, stack);
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
    printf("%d\n", stack_top(&stack1)->val);
    stack_print(&stack1);
    stack_print(&stack1);
    stack_push(&stack1, 2);
    printf("%d\n", stack_top(&stack1)->val);
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
    printf("%d\n", stack_top(&stack1)->val);
    return 0;
}