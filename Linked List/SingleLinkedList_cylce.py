class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLLCycle:
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


    def has_Cycle(self):
        if self.find_Cycle() == None:
            return False
        else:
            return True
    
    def find_Cycle(self):
        if self.head == None or self.head.next == None:
            return None
        
        t = h = self.head
        while h != None and h.next != None:
            t = t.next
            h = h.next.next
            if t == h:
                return t
        
        return None


    def remove_Cycle(self):
        c = self.find_Cycle()
        if c == None:
            return
        
        print("\nNode at which Loop was detected at ", c.info)

        p = q = c
        len_cycle = 0
        while True:
            q = q.next
            len_cycle = len_cycle+1
            if p == q:
                break
        print("Nodes inside the Cycle:", len_cycle)

        len_remain = 0
        p = self.head
        while p != q:
            p = p.next
            q = q.next
            len_remain = len_remain+1
        print("Remaining Nodes are:", len_remain)

        total_list_len = len_cycle+len_remain
        print("Total Nodes present in the List:", total_list_len)

        p = self.head
        for i in range(total_list_len-1):
            p = p.next
        p.next = None
        del i


    def insert_Cycle(self, data):
        if self.head == None:
            return
        
        p = self.head
        ptr = None
        while p != None:
            if p.info == data:
                ptr = p
            q = p
            p = p.next
        if ptr != None:
            q.next = ptr
        else:
            print(data, " not found !")



if __name__ == "__main__":
    objct = SLLCycle()
    objct.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes.")
        print("3. Insert Cycle.")
        print("4. Detect Cycle.")
        print("5. Delete Cycle.")
        print("6. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            objct.append(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            data = int(input("\nEnter the Node at which Cycle to be processed: "))
            objct.insert_Cycle(data)
            print("\nInsertion Done !")
        elif option == 4:
            if not objct.has_Cycle():
                print("\nNo Cycle Detected !")
            else:
                print("\nCycle Detected !")
        elif option == 5:
            objct.remove_Cycle()
            print("\nCycle has beed Removed check the List !")
        elif option == 6:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
    
    print("\n")

