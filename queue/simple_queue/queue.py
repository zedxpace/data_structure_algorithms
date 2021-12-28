##Queue Implementation

class queue:
    def __init__(self ):
        self.queue = []

    def enqueue(self ,element):
        self.queue.append(element)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def print_queue(self):
        print(self.queue)

##An empty queue    
qu = queue()

##enqueue operation
qu.enqueue(0)
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)

##print queue
qu.print_queue()

##dequeue operation
qu.dequeue()
qu.dequeue()

qu.print_queue()

