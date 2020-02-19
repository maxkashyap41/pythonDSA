class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLL_mergeSort:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head == None:
            print("\nList is Empty !")
        else:
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
    
    def merge(self, p, q):
        if p.info <= q.info:
            startM = p
            p = p.next
        else:
            startM = q
            q = q.next
        
        ptr = startM
        while p != None and q != None:
            if p.info <= q.info:
                ptr.next = p
                p = p.next
            else:
                ptr.next = q
                q = q.next
            ptr = ptr.next
        
        while p != None:
            ptr.next = p
            p = p.next
            ptr = ptr.next
        while q != None:
            ptr.next = q
            q = q.next
            ptr = ptr.next
        
        return startM
    
    def dividelist(self, list_head):
        if list_head == None:
            return 

        p = list_head
        q = list_head
        while q.next != None and q.next.next != None:
            p = p.next
            q = q.next
        head2 = p.next
        p.next = None
        return head2
    
    def Sort(self, list_head):
        if list_head == None or list_head.next == None:
            return list_head

        head1 = list_head
        head2 = self.dividelist(list_head)
        
        head1 = self.Sort(head1)
        head2 = self.Sort(head2)
        
        startM = self.merge(head1, head2)

        return startM

    def mergeSort(self):
        self.head = self.Sort(self.head)




if __name__ == "__main__":
    objct = SLL_mergeSort()
    objct.create_list()


    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes from End.")
        print("3. Merge Sort by Recursion.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            objct.append(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            objct.mergeSort()
            print("\nSorting done check the Updated List.")
        elif option == 4:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")