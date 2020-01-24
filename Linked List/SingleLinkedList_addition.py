class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
    

class SLLAdition:
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
        p = self.head
        r = None
        while p != None:
            q = p.next
            p.next = r
            r = p
            p = q
        self.head = r
    

    def addition(self, list2):
        p = self.head
        q = list2.head

        add_list = SLLAdition()
        carry = 0
        while p != None or q != None:
            if not p:
                i = 0
            else:
                i = p.info
            if not q:
                j = 0
            else:
                j = q.info
            sum = i+j+carry
            if sum >= 10:
                carry = 1
                rem = sum % 10
                if p.next == None or q.next == None:
                    c = 0
                    c_node = Node(c)
                    p.next = c_node
                    add_list.append(rem)
                else:
                    add_list.append(rem)
            else:
                carry = 0
                add_list.append(sum)
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        add_list.reverse_list()
        return add_list




if __name__ == "__main__":
    list1 = SLLAdition()
    list2 = SLLAdition()

    list1.create_list()
    list2.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes.")
        print("3. Addition of Two Lists.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            print("\nFirst List is: ", end = " ")
            list1.traversal()
            print("\nSecond List is: ", end = " ")
            list2.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value in List1: "))
            list1.append(data)
            data = int(input("\nEnter the new value in List2: "))
            list2.append(data)
            print("\nInsertion done check the Updated Lists.")
        elif option == 3:
            list1.reverse_list()
            list2.reverse_list()
            list3 = list1.addition(list2)
            print("\nNew Addition List is: ", end = " ")
            list3.traversal()
            #print("\nAddition done check the updated List.")
        elif option == 4:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
    
    print("\n")
