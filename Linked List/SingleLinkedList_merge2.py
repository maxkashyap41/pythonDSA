# merging the sorted list by rearranging the links

class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
    
class SLLMerging2:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            print("\nList is Empty !")
        else:
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
    
    def merging_the_list(self, list2):
        objct = SLLMerging2()
        objct.head = self.merge(self.head, list2.head)
        return objct
    
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
        
        if p == None:
            ptr.next = q
            q = q.next
            ptr = ptr.next
        else:
            ptr.next = p
            p = p.next
            ptr = ptr.next
        
        return startM
    

if __name__ == "__main__":
    list1 = SLLMerging2()
    list2 = SLLMerging2()

    list1.create_list()
    list2.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes from End.")
        print("3. Bubble Sorting using the Links but not the Data.")
        print("4. Merging the Sorted Linked List.")
        print("5. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            print("\nFirst List: ", end = " ")
            list1.traversal()
            print("\nSecond List: ", end = " ")
            list2.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value in list1: "))
            list1.append(data)
            data = int(input("\nEnter the new value in list2: "))
            list2.append(data)
            print("\nInsertion done check the Updated Lists.")
        elif option == 3:
            list1.bubblesort_link()
            list2.bubblesort_link()
            print("\nSorting done check the Updated Lists.")
        elif option == 4:
            mrg_objct = list1.merging_the_list(list2)
            print("\nMerged list is: ", end = " ")
            mrg_objct.traversal()
        elif option == 5:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")
