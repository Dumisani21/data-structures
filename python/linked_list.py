class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LL:
    
    def __init__(self):
        self.head = None
        
    def print_list(self):
        if self.head is None:
            print("Empty List")
            return
        
        itr = self.head
        itr_str = ""
        while itr:
            itr_str += str(itr.data) + ","
            itr = itr.next
        print(itr_str)

    
    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        
        itr.next = Node(value)
        
# linkedL = LL()

# linkedL.add(1)
# linkedL.add(2)
# linkedL.add(3)
# # linkedL.print_list()
# node_itr = linkedL.head
# while node_itr is not None:
#     print(node_itr.data)
#     node_itr = node_itr.next

print(dir(LL))