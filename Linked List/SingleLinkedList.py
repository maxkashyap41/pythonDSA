class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head == None:
            print("List is Empty !")
            return
        else:
            print("List is : ")
            p = self.head
            while p != None:
                print(p.info, "->", end=" ")
                p = p.next
            print("\n")
    
    def count_nodes(self):
        count = 0
        p = self.head
        while p != None:
            count = count+1
            p = p.next
        print("The Number of Nodes are: ", count)
    
    def search