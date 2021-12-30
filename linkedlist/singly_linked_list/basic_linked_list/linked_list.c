#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};

void print_linked_list(struct node *HEAD){
    while(HEAD != NULL){
        printf("%d\t" ,HEAD->data);
        HEAD = HEAD->next;
    }
}

int main(){
    struct node *HEAD;
    
    struct node *first = NULL;
    struct node *scnd  = NULL;

    first = malloc(sizeof(struct node));
    scnd  = malloc(sizeof(struct node));

    first->data = 1;

    scnd->data = 2;
    first->next = scnd;

    scnd->next = NULL;

    HEAD = first;
    
    print_linked_list(HEAD);
    return 0;
}