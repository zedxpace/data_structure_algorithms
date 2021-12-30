##Implmentation of Circular linked list

class node:
    def __init__(self ,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.HEAD = None

def print_linked_list(Head):
    while Head != None:
        print(Head.data ,"\t")

        Head = Head.next


if __name__ == '__main__':
    link_list = linked_list()

    one = node(0)
    two = node(1)
    three = node(2)
    four = node(3)

    one.next = two
    two.next = three
    three.next = four

    link_list.HEAD = one

    four.next = link_list.HEAD

    ##This will result in infinite loop which clearly states that one we reach at end of the linked list we will start traversing it from head again
    print_linked_list(link_list.HEAD)
