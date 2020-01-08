class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLLreverseGrp:
    def __init__(self):
        self.head = None
    

    def traversal(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        
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
        num = int(input("\nEnter the Number of Nodes: "))
        if num == 0:
            return
        print("\nEnter the values for the Nodes: ")
        for i in range(num):
            i = int(input())
            self.append(i)


    def reverse_list(self):
        if self.head == None:
            
    


    if __name__ == "__main__":
    objct = SLLaddOne()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes.")
        print("3. Reversing the List.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            objct.append(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            sum1 = objct.adding_one()
            sum1.traversal()
            #print("\nAddition done check the updated List.")
        elif option == 4:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
    
    print("\n")
