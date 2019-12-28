class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLLSorting:
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
        num = int(input("\nEnter the Number of Nodes: "))
        print("\nEnter the values for the Nodes: ")
        for data in range(num):
            data = int(input())
            self.insert_at_end(data)

    def insert_in_between_after_node(self, x, data):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        new = Node(data)
        p = self.head
        while p != None:
            if p.info == x:
                break
            p = p.next
        if p == None:
            print(x, " not found !")
            return
        else:
            new.next = p.next
            p.next = new
    
    def insert_in_between_before_node(self, x, data):
        if self.head == None:
            print("\nList is Empty !")
            return

        new = Node(data)
        if self.head == x:
            new.next = self.head
            self.head = new
        
        p = self.head
        while p != None:
            if p.next.info == x:
                break
            p = p.next
        if p == None:
            print(x, " not found !")
            return
        else:
            new.next = p.next
            p.next = new
    
    def bubblesort_data(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        end = None
        while end != self.head.next:
            p = self.head
            while p.next != end:
                q = p.next
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.next
            end = p

    def bubblesort_link(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        end = None
        while end != self.head.next:
            r = p = self.head
            while p.next != end:
                q = p.next
                if p.info > q.info:
                    p.next = q.next
                    q.next = p
                    if p != self.head:
                        r.next = q
                    else:
                        self.head = q
                    p, q = q, p
                r = p
                p = p.next
            end = p        
                

# Menu Driven Function

if __name__ == "__main__":
    node_ob = SLLSorting()
    node_ob.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Insert Node at End.")
        print("3. Insert in between *AFTER* Node.")
        print("4. Insert in between *BEFORE* Node.")
        print("5. Bubble Sorting using the Data but not the Links.")
        print("6. Bubble Sorting using the Links but not the Data.")
        print("7. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            node_ob.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            node_ob.insert_at_end(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            x = int(input("\nEnter the Node after which new value to be inserted: "))
            data = int(input("\nEnter the new value: "))
            node_ob.insert_in_between_after_node(x, data)
            print("\nInsertion done check the Updated List.")
        elif option == 4:
            x = int(input("\nEnter the Node before which new value to be inserted: "))
            data = int(input("\nEnter the new value: "))
            node_ob.insert_in_between_before_node(x, data)
            print("\nInsertion done check the Updated List.")
        elif option == 5:
            node_ob.bubblesort_data()
            print("\nSorting done check the Updated List.")
        elif option == 6:
            node_ob.bubblesort_link()
            print("\nSorting done check the Updated List.")
        elif option == 7:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")