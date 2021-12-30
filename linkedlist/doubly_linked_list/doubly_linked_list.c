#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    
    struct node *prev;
    struct node *next;
};

void insert_at_begining(struct node **head_ref ,int data){

    struct node *tmp_node = (struct node *)malloc(sizeof(struct node));

    tmp_node->data = data;
    tmp_node->prev = NULL;

    if((*head_ref) != NULL){
        (*head_ref)->prev = tmp_node;
    }

    tmp_node->next = *head_ref;
    (*head_ref) = tmp_node;
}

void insert_in_mid(struct node **head ,int data ,int indx){
    struct node *tmp = (struct node *)malloc(sizeof(struct node));
    tmp->data = data;
    
    int count = 0;
    struct node *tmp_head = *head;
    while(count != indx && tmp_head != NULL){
        count++;
        tmp_head = tmp_head->next;
    }

    tmp->next = tmp_head->next;
    tmp->prev = tmp_head;
    tmp_head->next = tmp;
}

void print_linked_list(struct node *head_ref){
    struct node *tmp_head;
    while(head_ref != NULL){
        int prev_data = -1;
        int next_data = -1;
        if(head_ref->prev != NULL){
            prev_data = head_ref->prev->data;
        }
        if(head_ref->next != NULL){
            next_data = head_ref->next->data;
        }
        
        printf("(prev : %d ,curr : %d ,next : %d) \t" ,prev_data ,head_ref->data  ,next_data);

        head_ref = head_ref->next;
        tmp_head = head_ref;
    }

}

int main(){
    struct node *HEAD = NULL;

    insert_at_begining(&HEAD ,0);
    insert_at_begining(&HEAD ,1);
    insert_at_begining(&HEAD ,2);
    insert_at_begining(&HEAD ,3);

    //print_linked_list(HEAD);

    insert_in_mid(&HEAD ,20 ,1);

    print_linked_list(HEAD);

    return 0;
}

