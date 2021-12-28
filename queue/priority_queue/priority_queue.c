//Implementing priority queue

#include <stdio.h>

#define MAX 5

int SIZE = 0;
int priority_queue[MAX];

//Method to swap the numbers
void swap(int *A ,int *B){
    int tmp = *A;
    *A = *B;
    *B = tmp;
}

/**
 * @brief 
 * 
 * 
 * @param indx 
 */
void heapify(int SIZE ,int indx){
    if(SIZE == 1){
        printf("Single Element in the Heap");
    }
    else{
        //Find LARGEST among ROOT ,LEFT child and RIGHT child
        int LARGEST = indx;

        int L = 2 * indx + 1;
        int R = 2 * indx + 2;

        if(L < SIZE && priority_queue[L] > priority_queue[LARGEST]){
            LARGEST = L;
        }
        
        if(R < SIZE && priority_queue[R] > priority_queue[LARGEST]){
            LARGEST = R;
        }

        //Swap and Continue heapifying if ROOT is not LARGEST
        if(LARGEST != indx){
            swap(&priority_queue[indx] ,&priority_queue[LARGEST]);

            heapify(SIZE ,LARGEST);
        }
    }
}

//Method to insert the element
void insert(int element){
    //if queue is FULL
    if(SIZE == MAX){
        printf("priority queue is FULL");
    }
    //If queue was EMPTY
    else if(SIZE ==0){
        priority_queue[0] = element;
        SIZE += 1;
    }
    //If queue has some elements
    else{
        priority_queue[SIZE] = element;
        SIZE +=1;
        //Start heapifying the queue
        for(int indx = 0 ;indx < SIZE ;indx++){
            heapify(SIZE ,indx);
        }
    }
}

//Method to remove an element from the queue
void delete(int element){
    int indx = 0;
    //Search for an element in the queue
    for(indx = 0 ;indx < SIZE ;indx++){
        if(element == priority_queue[indx]){
            break;
        }
    }
    
    //If we found an element then replace it with the last element of queue and reduce SIZE of an array by 1
    swap(&priority_queue[indx] ,&priority_queue[SIZE-1]);
    SIZE -=1;

    //Start heapifying the queue
    for(int indx = SIZE/2 - 1 ;indx >= 0 ;indx--){
        heapify(SIZE ,indx);
    }
}

//Print queue
void print_queue(){
    for(int indx = 0 ;indx < SIZE ;indx++){
        printf("-> %d" ,priority_queue[indx]);
    }

    printf("\n");
}

//Main
int main(){
    insert(0);
    insert(1);
    insert(2);
    insert(3);
    insert(4);

    print_queue();

    delete(2);

    print_queue();
}