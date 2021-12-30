#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};

void insert_at_begining(struct node **head_ref ,int data){
    struct node *tmp_node = (struct node *)malloc(sizeof(struct node));

    tmp_node->data  = data;
    tmp_node->next = (*head_ref);

    (*head_ref) = tmp_node;
}

void print_linked_list(struct node *head){
    while(head != NULL){
        printf("%d\t" ,head->data);

        head = head->next;
    }
}

int main(){

    struct node *HEAD;

    insert_at_begining(&HEAD ,0);
    insert_at_begining(&HEAD ,1);
    insert_at_begining(&HEAD ,2);
    insert_at_begining(&HEAD ,3);

    print_linked_list(HEAD);

    return 0;
}