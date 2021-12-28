//Implement cirular queue

#include <stdio.h>

#define MAX 5

int circ_queue[MAX];
int FRONT = -1;
int TAIL  = -1;

void enqueue(int element){
    if ((TAIL + 1) % MAX == FRONT || (FRONT == TAIL + 1)){
        printf("circular queue is FULL\n");
    }
    else if(FRONT == -1){
        FRONT = 0;
        TAIL  = 0;

        circ_queue[TAIL] = element; 
    }
    else{
        TAIL = (TAIL + 1) % MAX;
        circ_queue[TAIL] = element;
    }

}

void dequeue(){
    if (FRONT == -1){
        printf("circular queue is EMPTY\n");
    }
    else if(FRONT == TAIL){
        int tmp = circ_queue[FRONT];
        FRONT = -1;
        TAIL  = -1;

    }
    else{
        int tmp = circ_queue[FRONT];

        FRONT = (FRONT + 1)%MAX;

    }
}

void print_circ_queue(){
    if(FRONT == -1){
        printf("circular queue is EMPT-Y\n");
    }
    else{
        for(int indx = FRONT ;indx < TAIL ;indx = (indx + 1)%MAX){
            printf("-> %d" ,circ_queue[indx]); 
        }
    }

    printf("\n");
    
}

int main(){
    //enqueue operation
    enqueue(0);
    enqueue(1);
    enqueue(2);
    print_circ_queue();
    enqueue(3);
    enqueue(4);

    print_circ_queue();

    dequeue();
    dequeue();

    print_circ_queue();

    enqueue(5);

    print_circ_queue();

    return 0;
}