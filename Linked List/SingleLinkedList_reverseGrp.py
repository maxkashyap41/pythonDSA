class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLrevG:
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
    

    def reverseGrp(self, start, k):
        p = start
        q = None
        r = None
        count = 0
        while p != None and count < k:
            q = p.next
            p.next = r
            r = p
            p = q
            count = count+1
        if p != None:
            start.next = self.reverseGrp(p, k)
        
        return r




if __name__ == "__main__":
    node_ob = SLLrevG()
    node_ob.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes at End.")
        print("3. Reverse the List at kth.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            node_ob.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            node_ob.append(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            k = int(input("\nEnter the kth position: "))
            node_ob.head = node_ob.reverseGrp(node_ob.head, k)
            print("\nReverse Done check the Updated List !")
        elif option == 4:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")
        