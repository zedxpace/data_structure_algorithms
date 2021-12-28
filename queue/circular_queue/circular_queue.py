##Implementation of Circular queue

class circular_queue:

    def __init__(self ,size):
        self.size = size
        self.circ_queue = [None]*size

        self.FRONT = -1
        self.TAIL  = -1

    def enqueue(self ,element):
        if (self.TAIL + 1)%self.size == self.FRONT:
            print("circular queue is FULL")
        elif self.FRONT == -1:
            self.FRONT = 0
            self.TAIL = 0

            self.circ_queue[self.TAIL] = element
        else:
            self.TAIL = (self.TAIL + 1)%self.size
            self.circ_queue[self.TAIL] = element
    
    def dequeue(self):
        if self.FRONT == -1:
            print("queue is EMPTY")
        elif(self.FRONT == self.TAIL):
            tmp = self.circ_queue[self.FRONT]
            self.FRONT = -1
            self.TAIL  = -1
            return tmp
        else:
            tmp = self.circ_queue[self.FRONT]
            self.FRONT = (self.FRONT + 1)%self.size
            return tmp
    
    def print_circ_queue(self):
        if self.FRONT  == -1:
            print("circular queue is EMPTY")
        elif self.TAIL >= self.FRONT:
            for indx in range(self.FRONT ,self.TAIL+1):
                print(self.circ_queue[indx] ,end=" ")
        else:
            
            for indx in range(0 ,self.TAIL+1):
                print(self.circ_queue[indx] ,end=" ")

            for indx in range(self.FRONT ,self.size):
                print(self.circ_queue[indx] ,end=" ")
            

        print("\n") 
circ_queue = circular_queue(5)


##enqueue operation
circ_queue.enqueue(0)
circ_queue.enqueue(1)
circ_queue.enqueue(2)            
circ_queue.enqueue(3)
circ_queue.enqueue(4)

#print queue
circ_queue.print_circ_queue()

#more enqueue operation
circ_queue.enqueue(5)

#print queue
circ_queue.print_circ_queue()

#dequeue operation
circ_queue.dequeue()
circ_queue.dequeue()
circ_queue.dequeue()

#print queue
circ_queue.print_circ_queue()

#more enqueue operation
circ_queue.enqueue(5)

#print queue
circ_queue.print_circ_queue()
