MAX = 3

class proc_details:
    def __init__(self ,pid ,pname):
        self.proc_id = pid 
        self.pname = pname


class circ_queue:
    def __init__(self):
        self.cqueue = [None]*MAX

        self.FRONT = -1
        self.REAR  = -1

    def is_empty(self):
        if self.REAR == -1:
            return True

        return False

    def is_full(self):
        if (self.REAR + 1) % MAX == self.FRONT:
            return True
        return False

    def enqueue(self ,data):
        print(self.REAR ," " ,self.FRONT)
        if self.FRONT == -1 and self.REAR == -1:
            self.FRONT += 1
            self.REAR += 1
        elif not self.is_full:
            self.REAR += 1
        else :
            self.REAR = (self.REAR + 1) % MAX

        self.cqueue[self.REAR] = data

    def dequeue(self ):
        if not self.is_empty():
            data = self.cqueue.pop(0)
            if self.FRONT == self.REAR:
                self.FRONT = -1
                self.REAR  = -1
                
                self.cqueue = [None]* MAX
            else:
                self.FRONT = (self.FRONT + 1) % MAX
            
            return data
        
        return True
    
    def print_circ_queue(self):
        print("--printing--")
        for proc in self.cqueue:
            print("%d process's in queue"%(self.REAR))
            print("caller details : ")
            obj = proc
            print("id : " ,obj.proc_id)
            print("name : " ,obj.pname)

            print("\ncprocess exeuted - Next process in queue")
            

dic = {
    1 : "xos" ,
    2  : "firefx" ,
    3 : "gbrom" 
}

cqueue = circ_queue()

for i in (dic):
    pd = proc_details(i ,dic[i])
    cqueue.enqueue(pd)

while cqueue.REAR > -1:
    print("%d process's in queue"%(i))
    print("caller details : ")
    obj = cqueue.dequeue()
    print("id : " ,obj.proc_id)
    print("name : " ,obj.pname)

    print("\ncprocess exeuted - Next process in queue")

print("--No more process in queue--")

pd = proc_details(12 ,'ios')
cqueue.enqueue(pd)
pd = proc_details(13 ,'soc')
cqueue.enqueue(pd)
pd = proc_details(14 ,'ip')
cqueue.enqueue(pd)
pd = proc_details(15 ,'p')
cqueue.enqueue(pd)

cqueue.print_circ_queue()

