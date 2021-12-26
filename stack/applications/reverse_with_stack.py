MAX = 10


class stack:
    def __init__(self):
        self.stack = []
        self.TOP = -1

    def is_full(self):
        if MAX == len(self.stack):
            return True
        return False

    def is_empty(self):
        if self.TOP == -1:
            return True
        return False
    
    def push(self ,wrd):
        if not self.is_full():
            self.stack.append(wrd)
            self.TOP += 1
        return "FULL"
    
    def pop(self):
        if not self.is_empty():
            wrd = self.stack.pop(self.TOP)
            self.TOP -= 1
            return wrd
        return "EMPTY"

    
stack = stack()

word = "saransh"

for i in range(len(word)):
    stack.push(word[i])

while stack.TOP > -1:
    print(stack.pop())