# merging the sorted list by making another linked list

class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SLLMerging1:
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
        if num == None:
            return
        print("\nEnter the values for the Nodes: ")
        for data in range(num):
            data = int(input())
            self.insert_at_end(data)

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
    
    def merging_the_list(self, list2):
        ob_mrge = SLLMerging1()
        ob_mrge.head = self.merge(self.head, list2.head)
        return ob_mrge

    def merge(self, p, q):
        if p.info <= q.info:
            new_M = Node(p.info)
            p = p.next
        else:
            new_M = Node(q.info)
            q = q.next
        
        # now we keep a pointer to track the min value of the 2 list
        ptr = new_M
        while p != None and q != None:
            if p.info <= q.info:
                ptr.next = Node(p.info)
                p = p.next
            else:
                ptr.next = Node(q.info)
                q = q.next
            ptr = ptr.next
        
        while p != None:
            ptr.next = Node(p.info)
            p = p.next
            ptr = ptr.next
        while q != None:
            ptr.next = Node(q.info)
            q = q.next
            ptr = ptr.next
        
        return new_M


if __name__ == "__main__":
    list1 = SLLMerging1()
    list2 = SLLMerging1()

    list1.create_list()
    list2.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Insert Node at End.")
        print("3. Bubble Sorting using the Data but not the Links.")
        print("4. Bubble Sorting using the Links but not the Data.")
        print("5. Merging the Sorted Linked List.")
        print("6. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            print("\nFirst List: ", end = " ")
            list1.traversal()
            print("\nSecond List: ", end = " ")
            list2.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value in list1: "))
            list1.insert_at_end(data)
            data = int(input("\nEnter the new value in list2: "))
            list2.insert_at_end(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            list1.bubblesort_data()
            list2.bubblesort_data()
            print("\nSorting done check the Updated List.")
        elif option == 4:
            list1.bubblesort_link()
            list2.bubblesort_link()
            print("\nSorting done check the Updated List.")
        elif option == 5:
            list3 = list1.merging_the_list(list2)
            print("\nMerged List is: ", end = " ")
            list3.traversal()
        elif option == 6:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")