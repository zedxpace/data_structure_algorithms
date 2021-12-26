import webbrowser

class prev_surfed_links:
    def __init__(self ,link):
        self.link = link

class stack:
    MAX = 10
    
    def __init__(self):
        self.stack = [''] * self.MAX
        self.TOP   = -1
    
    def is_full(self):
        return self.TOP == self.MAX
    
    def is_empty(self):
        return self.TOP == -1
    
    def push(self ,link):
        self.TOP += 1
        self.stack[self.TOP] = link

    
    def pop(self):
        self.stack[self.TOP] = None
        self.TOP -= 1
        
    
    def peek(self):
        return self.stack[self.TOP]
    
    def print_stack(self):
        tmp = self.TOP

        while tmp >= 0:
            print(self.stack[tmp].link)
            tmp -= 1


if __name__ == '__main__':
    stack = stack()

    for i in range(2):
        link = str(input('enter the link you want to surf : '))
        stack.push(prev_surfed_links(link))
    
    stack.print_stack()

    print(stack.pop())

