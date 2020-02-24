class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
    

class SLLrotateList:
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

    
    def rotateList(self, k):
        count = 1
        temp = None
        p = self.head
        while p.next != None:
            if count == k:
                ptr = p
                p = p.next
                temp = self.head
                self.head = ptr.next
                ptr.next = None
            if p.next != None:
                p = p.next
                count = count+1
            else:                   # for TC : 12 -> 26 -> None
                continue
        p.next = temp




if __name__ == "__main__":
    objct = SLLrotateList()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Rotate the Linked List according to kth position.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            objct.append(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            k = int(input("\nEnter the kth value to rotate: "))
            objct.rotateList(k)
            print("\nRotation Done check the Updated List.")
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")