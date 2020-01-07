class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLLaddOne:
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
        num = int(input("\nEnter the Number of Nodes: "))
        if num == 0:
            return
        
        print("\nEnter the values for the Nodes: ")
        for i in range(num):
            i = int(input())
            self.append(i)

    
    def reverse_list(self):
        p = self.head
        r = None
        while p != None:
            q = p.next
            p.next = r
            r = p
            p = q
        self.head = r
    
    
    def adding_one(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        add = SLLaddOne()
        self.reverse_list()
        
        carry = 0
        sum = self.head.info+1
        if sum >= 10:
            carry = 1
            rem = sum%10
            add.append(rem)
        else:
            carry = 0
            add.append(sum)

        p = self.head.next
        while p != None:
            sum = p.info+carry
            if sum >= 10:
                carry = 1
                rem = sum%10
                if p.next == None and p.info == 9:
                    c = 0
                    new = Node(c)
                    p.next = new
                    add.append(rem)
                else:
                    add.append(rem)
            else:
                carry = 0
                add.append(sum)
            p = p.next
        add.reverse_list()
        return add
    


if __name__ == "__main__":
    objct = SLLaddOne()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes.")
        print("3. Addition of One at Last Node.")
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