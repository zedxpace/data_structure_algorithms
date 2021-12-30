#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};

//swapping method
void swap(int *num1 ,int *num2){
    int tmp = *num1;
    *num1   = *num2;
    *num2   = tmp;
}

//insert at beginning
void insert_at_begining(struct node **head_ref  ,int data){
    struct node *tmp_node = (struct node*)malloc(sizeof(struct node));

    //insert data into the newly created node
    tmp_node->data = data;
    //set the link of newly created to node pointed by head 
    tmp_node->next = (*head_ref);
    //set the head to the newly created node since the motive is to add the node 
    (*head_ref) = tmp_node;
}

//insert node after specific node 
void insert_after(struct node *prev_node ,int data){
    if(prev_node == NULL){
        return;
    }

    struct node *tmp_node = (struct node*)malloc(sizeof(struct node));

    tmp_node->data = data;
    tmp_node->next = prev_node->next;
    prev_node->next = tmp_node;
}

//
void insert_node_at_last(struct node **head_ref ,int data){

    struct node *tmp_node = (struct node*)malloc(sizeof(struct node));
    tmp_node->data = data;
    tmp_node->next = NULL;

    if(head_ref == NULL){
        *head_ref = tmp_node;
        NULL;
    }

    struct node *last_node = *head_ref;
    
    while(last_node->next != NULL){
        last_node = last_node->next;
    }

    last_node->next = tmp_node;
}

//
void delete_node(struct node **head_ref ,int key){
    struct node *tmp_head_node = *head_ref ,*tmp_prev_node;

    if(tmp_head_node != NULL && tmp_head_node->data  == key){
        *head_ref = tmp_head_node->next;

        free(tmp_head_node);

        return;
    }

    while(tmp_head_node != NULL && tmp_head_node->data != key){
        tmp_prev_node = tmp_head_node;

        tmp_head_node = tmp_head_node->next;
    }

    if(tmp_head_node == NULL){
        return;
    }

    //remove the node
    tmp_prev_node->next = tmp_head_node->next;
    free(tmp_head_node);
}

int search_node(struct node **head_ref ,int data){

    struct node *tmp_node = *head_ref;

    while(tmp_node != NULL){
        if(tmp_node->data == data){
            tmp_node = tmp_node->next;
        }
        
    }
    return 0;
}

void sort_node(struct node *head ){
    struct node *curr_node = head;

    while(curr_node != NULL){
        struct node *next_node = curr_node->next;

        while(next_node != NULL){
            if(curr_node->data > next_node->data){
                swap(&curr_node->data ,&next_node->data);
            }

            next_node = next_node->next;
        }

        curr_node = curr_node->next;
    }
}

void print_linked_list(struct node *node){

    while(node != NULL){
        printf("%d\t" ,node->data);
        node = node->next;
    }

    printf("\n");
}

int main(){
    struct node *head = NULL;

    insert_at_begining(&head ,9);
    insert_at_begining(&head ,43);
    insert_at_begining(&head ,24);
    insert_at_begining(&head ,3);

    print_linked_list(head);

    insert_node_at_last(&head ,4);

    print_linked_list(head);

    delete_node(&head ,0);

    print_linked_list(head);

    insert_after(head->next->next ,9);

    print_linked_list(head);

    sort_node(head);

    print_linked_list(head);
}