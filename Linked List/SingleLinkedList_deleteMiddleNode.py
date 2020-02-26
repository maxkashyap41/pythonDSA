class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
    

class SLLdeleteMidNode:
    def __init__(self):
        self.head = None


    def traversal(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        print("\nList is: ", end = " ")
        p = self.head
        while p != None:
            print(p.info, end = " ")
            p = p.next
        print("\n")


    def append(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return
        
        p = self.head
        while p.next != None:
            p = p.next
        p.next = new
    

    def create_list(self):
        num = int(input("\nEnter the number of Nodes: "))
        if num == 0:
            return
        
        print("\nEnter the values for the Nodes: ")
        for i in range(num):
            i = int(input())
            self.append(i)
    

    def deleteNode(self):
        if self.head == None:
            return
    
        p = self.head
        q = self.head
        r = None
        while q != None and q.next != None:
            q = q.next.next
            r = p
            p = p.next
        r.next = p.next



if __name__ == "__main__":
    objct = SLLdeleteMidNode()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Delete the Middle Node.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            objct.append(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            objct.deleteNode()
            print("\nDeletion Done check the Updated List.")
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")