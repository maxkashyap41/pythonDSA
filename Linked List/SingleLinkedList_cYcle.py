class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLcYcle:
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
    

    def insertcYcle(self, data):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        p = self.head
        ptr = None
        while p != None:
            if p.info == data:
                ptr = p
            r = p
            p = p.next
        if ptr != None:
            r.next = ptr
        else:
            print("\n", data, "not found !")

    
    def findcYcle(self):
        if self.head == None or self.head.next == None:
            return None
        
        t = self.head
        h = self.head
        while h != None and h.next != None:
            t = t.next
            h = h.next.next
            if t == h:
                return t
        return None
    

    def HAScYcle(self):
        if self.findcYcle() != None:
            return True
        else:
            return False
    

    def removecYcle(self):
        c = self.findcYcle()
        if c == None:
            return
        
        print("\nNode at which cYcle was detected is",c.info)

        p = q = c
        len_cycle = 0
        while True:
            q = q.next
            len_cycle = len_cycle+1
            if q == p:
                break
        print("Nodes inside the cYcle: ", len_cycle)

        p = self.head
        len_remain = 0
        while p != q:
            p = p.next
            q = q.next
            len_remain = len_remain+1
        print("Nodes outside the cYcle: ", len_remain)

        total_nodes = len_cycle+len_remain
        print("Total Nodes: ", total_nodes)

        p = self.head
        for i in range(total_nodes-1):
            p = p.next
        p.next = None
        del i    



if __name__ == "__main__":
    objct = SLLcYcle()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Insert CYCLE in the List.")
        print("4. Detect CYCLE in the List.")
        print("5. Remove CYCLE from the List.")
        print("6. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            objct.append(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            info = int(input("\nEnter the value at which CYCLE is to be inserted: "))
            objct.insertcYcle(info)
            print("\nInsertion of CYCLE done !")
        elif option == 4:
            if not objct.HAScYcle():
                print("\nNo CYCLE has been detected !")
            else:
                print("\nCYCLE has been detected !")
        elif option == 5:
            objct.removecYcle()
            print("\nCYCLE has been removed !")
        elif option == 6:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")
    
