#Implementation for linked list operations

class node:
    def __init__(self ,data):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        self.HEAD = None
    
    ##insert data at begining of linked-list
    def insert_at_begining(self ,data):
        tmp_node = node(data)

        tmp_node.next = self.HEAD
        self.HEAD = tmp_node

    ##insert data at ending of linked-list
    def insert_at_end(self ,data):
        tmp_node = node(data)

        if self.HEAD is None:
            self.HEAD = tmp_node
            return
        
        LAST = self.HEAD
        while( LAST.next):
            LAST = LAST.next
        
        LAST.next = tmp_node
    
    ##search for an element in the linked-list
    def search(self ,key):
        CURR = self.HEAD

        while CURR is not None:
            if CURR.data == key:
                return True
            
            CURR = CURR.next
        
        return False

    ##delete node from specific index
    def delete_element(self ,indx):

        if self.HEAD is None:
            return 
        
        tmp = self.HEAD

        if indx == 0:
            self.HEAD = tmp.next
            tmp = None
            return
        
        for i in range(indx - 1):
            tmp = tmp.next

            if tmp is None:
                return
        if tmp.next is None:
            return
        
        nxt = tmp.next.next
        tmp.next = None

        tmp.next = nxt
    
    ##insert node after specific node
    def insert_after(self ,prev_node ,data):

        if prev_node is None:
            return
        
        tmp_node = node(data)

        tmp_node.next = prev_node.next

        prev_node.next = tmp_node
    
    ##print linked-list
    def print_linked_list(self):
        tmp_node = self.HEAD

        while(tmp_node):
            print(tmp_node.data ),
            tmp_node = tmp_node.next
        
        print("\n")
    
    ##sort the linked_list
    def sort_linked_list(self):
        curr_node = self.HEAD

        while(curr_node):
            next_node = curr_node.next

            while next_node:
                if curr_node.data > next_node.data:
                    ##swap it
                    curr_node.data ,next_node.data = next_node.data ,curr_node.data

                next_node = next_node.next
            
            curr_node = curr_node.next
##
if __name__ == '__main__':

    link_list = linked_list()

    link_list.insert_at_begining(9)
    link_list.insert_at_begining(4)
    link_list.insert_at_begining(2)
    link_list.insert_at_begining(3)

    link_list.print_linked_list()

    link_list.insert_at_end(4)

    link_list.print_linked_list()

    link_list.sort_linked_list()

    link_list.print_linked_list()



    

