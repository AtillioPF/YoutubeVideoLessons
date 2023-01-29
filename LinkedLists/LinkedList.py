# Implementing a single linked list class with a internal node class

class node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class linked_list():
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
        cur_node.next = new_node
        
    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next!=None:
            total+=1
            cur_node=cur_node.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)