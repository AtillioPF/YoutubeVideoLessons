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
        
    def get(self, index):
        if index>=self.length():
            print("ERROR : 'Get' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index==index: return cur_node.data
            cur_index+=1
            
    def erase(self,index):
        if index>=self.length():
            print("ERROR : 'Erase' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if (cur_index==index):
                last_node.next = cur_node.next
                return
            cur_index+=1
            
        
my_list = linked_list()
    
my_list.display()

my_list.append("Atillio")

my_list.display()

my_list.append("Bethina")
my_list.append("Nico")
my_list.append("Paçoca")
my_list.display()

print(my_list.get(2))

my_list.erase(2)

my_list.display()