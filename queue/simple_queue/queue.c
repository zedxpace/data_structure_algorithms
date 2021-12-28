//Queue implementation

#include <stdio.h>
#include <stdlib.h>

#define MAX 10

int FRONT = -1;
int RARE = -1;

int queue[MAX];

void enqueue(int element){
    if(RARE == MAX-1){
        printf("queue is FULL");
    }
    else{
        if(FRONT == -1){
            FRONT = 0;
        }
        RARE++;
        queue[RARE] = element;
    }
}

void dequeue(){
    if(FRONT == -1){
        printf("queue is EMPTY");
    }
    else{
        FRONT++;
        if(FRONT > RARE){
            FRONT = RARE = -1;
        }
    }
}

void print_queue(){
    for(int indx = FRONT ;indx < RARE ;indx++){
        printf("-> %d" ,queue[indx]);
    }
}

int main(){
    dequeue();

    //Enqueue operation
    enqueue(0);
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);

    //print queue
    print_queue();

    //Dequeue operation
    dequeue();
    dequeue();

    printf("\n");
    print_queue();

}