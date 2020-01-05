class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLLReverse:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        else:
            print("\nList is: ", end = " ")
            p = self.head
            while p != None:
                print(p.info, end = " ")
                p = p.next
            print("\n")
    
    def insert_at_begin(self, data):
        new = Node(data)
        if self.head == None:
            print("\nList is Empty !")
            return

        new.next = self.head
        self.head = new

    def insert_at_end(self, data):
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
        if num == None:
            return
        print("\nEnter the values for the Nodes: ")
        for data in range(num):
            data = int(input())
            self.insert_at_end(data)

    def reverse_list(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        p = self.head
        r = None
        while p != None:
            q = p.next
            p.next = r
            r = p
            p = q
        self.head = r
    
    def reverse_list_recur(self, p, r):
        if not p:
            return r
        
        q = p.next
        p.next = r
        r = p
        p = q
        return self.reverse_list_recur(p, r)


    
    def reverse_list_arg(self):
        self.head = self.reverse_list_recur(self.head, None)


# Menu Driven Function
     
if __name__ == "__main__":
    node_ob = SLLReverse()
    node_ob.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Insert Node at Begin.")
        print("3. Insert Node at End.")
        print("4. Reverse the Linked List.")
        print("5. Reverse the Linked List using Recursion.")
        print("6. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            node_ob.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            node_ob.insert_at_begin(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            data = int(input("\nEnter the new value: "))
            node_ob.insert_at_end(data)
            print("\nInsertion done check the Updated List.")
        elif option == 4:
            node_ob.reverse_list()
            print("\nList has been Reversed check the Updated List !")
        elif option == 5:
            node_ob.reverse_list_arg()
            print("\nList has been Reversed check the Updated List !")
        elif option == 6:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
    
    print("\n")
