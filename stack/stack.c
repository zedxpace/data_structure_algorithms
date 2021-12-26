//Stack implementation
#include <stdio.h>
#include <stdlib.h>

#define MAX 10

int count = 0;

//create stack
struct stack{
    int elements[MAX];
    int TOP;
};

typedef struct stack stk;

//create an empty stack
void create_empty_stack(stk *stack){
    stack->TOP = -1;
}

//check if stack is FULL
int is_full(stk *stack){
    if(stack->TOP == MAX){
        return 1;
    }
    else{
        return 0;
    }
}

//check if stack is empty
int is_empty(stk *stack){
    if(stack->TOP == -1){
        return 1;
    }
    else{
        return 0;
    }
}

//Add an element into stack
void push(stk *stack ,int element){
    if(is_full(stack)){
        printf("Stack is FULL");
    }
    else{
        stack->TOP++;
        stack->elements[stack->TOP] = element;
    }

    count++;
}


//Pop an element from the stack
void pop(stk *stack ){
    if(is_empty(stack)){
        printf("stack is EMPTY");
    }
    else{
        stack->TOP--;
    }

    count--;
}

//Method to print stack
void print_stack(stk *stack){
    for(int indx = 0 ;indx < count ;indx++){
        printf("-> %d" ,stack->elements[indx]);
    }
    printf("\n");
}

int main(){
    int ch;

    stk *stack = (stk *)malloc(sizeof(stk));
    create_empty_stack(stack);

    push(stack ,1);
    push(stack ,2);
    push(stack ,3);
    push(stack ,4);

    print_stack(stack);

    //pop operation
    pop(stack);

    print_stack(stack);
}