##Implement Stack

##
def create_stack():
    stack = []
    return stack

##
def push(stack ,element ):
    stack.append(element )

##
def is_empty(stack ):
    return len(stack) == 0

##
def pop(stack ):
    if is_empty(stack ):
        print("Stack is empty")
        return
    return stack.pop()

##create a stack
stack = create_stack()

##push operation
push(stack ,0)
push(stack ,1)
push(stack ,2)
push(stack ,3)
push(stack ,4)

##print stack
print(stack)

##pop operation
pop(stack)
pop(stack)
print(stack)