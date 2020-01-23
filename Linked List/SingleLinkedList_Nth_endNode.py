# Nth node from end of linked list

class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLendNode:
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
    

    def getNth_end(self, n):        
        p = self.head
        count = 0
        n_th = 0
        while p != None:
            p = p.next
            count = count+1
        print("\nNodes are: ",count)

        p = self.head
        if n <= count:
            n_th = count-n+1
            for i in range(n_th-1):
                p = p.next
            del i
            val = p.info
            print("Expected Value is: ",val)
        else:
            print("No Value found, returning ",-1)





if __name__ == "__main__":
    objct = SLLendNode()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Get Nth Node from the Back.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            objct.append(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            n = int(input("\nEnter the Nth Node: "))
            objct.getNth_end(n)
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")