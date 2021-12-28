##Implementation of Deque

class deque:

    def __init__(self ):
        self.dque = []
    
    def is_empty(self ):
        return self.dque == []
    
    def insert_to_front(self ,element ):
        self.dque.insert(0 ,element)
    
    def insert_to_rear(self ,element ):
        self.dque.append(element)
    
    def delete_from_front(self ):
        self.dque.pop(0)
    
    def delete_from_rear(self ):
        self.dque.pop()
    
dque = deque()

##insertion operation at front
dque.insert_to_front(0)
dque.insert_to_front(1)
dque.insert_to_front(2)
dque.insert_to_front(3)

print(dque.dque)
##insertion operation at an end
dque.insert_to_rear(4)

print(dque.dque)

##delete opertaion at front
dque.delete_from_front()
dque.delete_from_front()

print(dque.dque)

##delete operation at an end
dque.delete_from_rear()

print(dque.dque)