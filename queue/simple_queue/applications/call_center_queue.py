MAX = 10

class caller:
    def __init__(self ,name ,phone):
        self.name = name 
        self.phone = phone

class queue:
    def __init__(self):
        self.queue = []

        self.FRONT = -1
        self.REAR  = -1
    
    def is_empty(self):
        if self.FRONT == -1 and self.REAR == -1:
            return True
        return False
    
    def is_full(self):
        if self.REAR == MAX:
            return True
        return False
    
    def enqueue(self ,data):
        if not self.is_full():
            self.queue.append(data)
            if self.FRONT == -1:
                self.FRONT += 1
            self.REAR += 1
        return "FULL"

    def dequeue(self):
        if not self.is_empty():
            data = self.queue.pop(0)
            self.REAR -= 1
            return data
        return "EMPTY"

dic = {
    "sara" : "+91-9817654320" ,
    "zed"  : "+91-9876543210" ,
    "addy" : "+91-0987654321"
}

queue = queue()

for i in (dic):
    callr = caller(i ,dic[i])
    queue.enqueue(callr)

for i in range(queue.REAR):
    print("%d caller in queue"%(i+1))
    print("caller details : ")
    obj = queue.dequeue()
    print("name : " ,obj.name)
    print("numb : " ,obj.phone)

    print("\ncall ended - Next caller in queue")

print("--No more calls in queue--")

