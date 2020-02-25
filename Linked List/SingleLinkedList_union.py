class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLunion:
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
    

    def appending(self, data):
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
            self.appending(i)
    

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
    

    def unionList(self, list2):
        p = self.head
        q = list2.head
        head = self.merge(p, q)

        arr = []
        p = head
        while p != None:
            arr.append(p.info)
            p = p.next
        
        # print(arr)
        arr.sort()
        new_arr = []
        for no in arr:
            if no not in new_arr:
                new_arr.append(no)
        # print(new_arr)

        # making new objct of the same corresponding Linked List to store the new_array eles
        objct = SLLunion() 
        for i in range(len(new_arr)):
            objct.appending(new_arr[i])
        
        return objct




if __name__ == "__main__":
    a = SLLunion()
    b = SLLunion()

    a.create_list()
    b.create_list()


    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Union of 2 Lists.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            a.traversal()
            b.traversal()
        elif option == 2:
            data = int(input("\nEnter the New data: "))
            a.appending(data)
            data = int(input("\nEnter the New data: "))
            b.appending(data)
            print("\nNode inserted check the List.")
        elif option == 3:
            newHead = a.unionList(b)
            newHead.traversal()
            print("\nUnion of List Done check the Updated List.")
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")