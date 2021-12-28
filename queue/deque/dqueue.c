#include <stdio.h>

#define MAX 10

int deque[MAX];
int front = -1;
int rare  = -1;

int count(){
    int cnt = 0;

    for(int indx = 0 ;indx < MAX ;indx++){
        if(deque[indx] != 0){
            cnt++;
        }
    }
    
    return cnt;
}

void add_front(int element ){
    if(front == 0 && rare == MAX - 1){
        printf("Deque is full");
    }

    if(front == -1){
        front = rare = 0;
        deque[front] = element;

        return;
    }

    if(rare != MAX - 1){
        int C = count();
        int K = rare + 1;

        for(int indx = 1 ;indx <= C ;indx++){
            deque[K] = deque[K - 1];
            K--;
        }

        deque[K] = element;
        front = K;
        rare++;
    }
    else{
        front--;

        deque[front] = element;
    }
}

void add_rare(int element){
    if(front == 0 && rare == MAX - 1){
        printf("deque is full");
    }

    if(front == -1){
        rare = front = 0;
        deque[rare] = element;

        return;
    }

    if(rare == MAX - 1){
        int K = front - 1;

        for(int indx = front - 1 ;indx < rare ;indx++){
            K = indx;

            if(K == MAX - 1){
                deque[K] = 0;
            }
            else{
                deque[K] = deque[indx + 1];
            }
        }
        rare--;
        front--;
    }
    rare++;
    deque[rare] = element;
}

int delete_from_front(){
    int element;

    if(front == -1){
        printf("deque is empty\n");
    }

    element = deque[front];

    deque[front] = 0;

    if(front == rare){
        front = rare = -1;
    }
    else{
        front++;
    }

    return element;
}

int delete_from_end(){
    int element;

    if(front == -1){
        printf("deque is empty");
    }

    element = deque[rare];
    deque[rare] = 0;

    rare--;
    if(rare == -1){
        front = -1;
    }

    return element;
}

void print(){
    for(int indx = 0 ;indx < MAX ;indx++){
        printf("%d -> " ,deque[indx]);
    }
    printf("\n");
}




int main(){
    //insertion at front
    add_front(0);
    add_front(1);
    add_front(2);

    print();

    //insertion at end
    add_front(4);

    print();

    //deletion at front
    delete_from_front();

    print();

    //deletion from end
    delete_from_end();

    print();

    return 0;
}