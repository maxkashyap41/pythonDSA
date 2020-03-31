class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLaddition:
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

        add_list = SLLaddition()
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
            
            _sum_ = i+j+carry
            if _sum_ >= 10:
                carry = 1
                rem = _sum_ % 10
                if p.next == None:
                    c = 0
                    c_node = Node(c)
                    p.next = c_node
                    add_list.append(rem)
                else:
                    add_list.append(rem)
            else:
                carry = 0
                add_list.append(_sum_)

            if p != None:
                p = p.next
            if q != None:
                q = q.next
        
        add_list.reverse_list()
        return add_list



if __name__ == "__main__":
    a = SLLaddition()
    b = SLLaddition()

    a.create_list()
    b.create_list()


    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Addition of 2 Lists.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            a.traversal()
            b.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            a.append(data)
            data = int(input("\nEnter the New data: "))
            b.append(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            a.reverse_list()
            b.reverse_list()
            c = a.addition(b)
            print("\nAddition: ", end = " ")
            c.traversal()
            
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")