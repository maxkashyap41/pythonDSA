class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
    

class SLLdeleteNode:
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
    

    def getNode(self, data):
        p = self.head
        while p.next != None and p.info != value:
            p = p.next
            if p.info == value:
                return p
        
        return None
    

    def deleteNode(self, delNode):
        # delNode it is the Node pointer
        temp = delNode
        k = delNode

        if temp.next == None:
            print("\nCannot Delete Last Node w/o head pointer!")
            return
        else:    
            while temp.next != None:
                temp.info = temp.next.info
                temp = temp.next
                if temp.next != None:
                    k = k.next
            k.next = None
                
    



if __name__ == "__main__":
    objct = SLLdeleteNode()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Delete a Node without Head Pointer.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            objct.append(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            value = int(input("\nEnter the value of the List u wanna Delete: "))
            delNode = objct.getNode(value)
            objct.deleteNode(delNode)
            print("\nDeletion Done check the Updated List.")
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")