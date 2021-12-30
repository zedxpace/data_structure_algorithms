#Implementation of Linked List

class node:
    def __init__(self ,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    link_list = linked_list()
    
    link_list.head = node(0)
    
    scnd = node(1)
    scnd.next = None

    link_list.head.next = scnd

    #traverse through linked-list
    while link_list.head != None:
        print(link_list.head.data ,end="\t")
        link_list.head = link_list.head.next