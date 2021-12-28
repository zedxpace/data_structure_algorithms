##Implement priority queue

class priority_queue:

    def __init__(self):
        self.prior_queue = []

    def insert(self ,element ):
        SIZE = len(self.prior_queue)
        if SIZE == 0:
            self.prior_queue.append(element)
        else:
            self.prior_queue.append(element)
            for indx in range((SIZE // 2) - 1 ,-1 ,-1):
                self.heapify(SIZE ,indx)
    
    def heapify(self ,SIZE ,indx):

        ##Find the largest among root ,left-child ,right-child

        LARGEST = indx
        L = 2 * indx + 1
        R = 2 * indx + 2

        if L < SIZE and self.prior_queue[indx] < self.prior_queue[L]:
            LARGEST = L
        
        if R < SIZE and self.prior_queue[indx] < self.prior_queue[R]:
            LARGEST = R
        
        if LARGEST != indx:
            ##swap and continue heapifying if root is not largest
            self.prior_queue[indx] ,self.prior_queue[LARGEST] = self.prior_queue[LARGEST] ,self.prior_queue[indx]
            self.heapify(SIZE ,indx)
    
    def delete(self ,element):
        SIZE = len(self.prior_queue)

        indx = 0
        for indx in range(0 ,SIZE):
            if element == self.prior_queue[indx]:
                break
        
        self.prior_queue[indx] ,self.prior_queue[SIZE-1] = self.prior_queue[SIZE-1] ,self.prior_queue[indx]

        self.prior_queue.remove(SIZE-1)

        for indx in range((len(self.prior_queue) // 2) - 1 ,-1 ,-1):
            self.heapify(len(self.prior_queue) ,indx)

prior_queue = priority_queue()

prior_queue.insert(0)
prior_queue.insert(1)
prior_queue.insert(3)
prior_queue.insert(2)
prior_queue.insert(4)

print(prior_queue.prior_queue)

prior_queue.delete(0)
prior_queue.delete(0)

print(prior_queue.prior_queue)

prior_queue.insert(5)

print(prior_queue.prior_queue)