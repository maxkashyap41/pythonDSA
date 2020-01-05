class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLL_swapPair:
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
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new
    
    def create_list(self):
        num = int(input("\nEnter the Number of Nodes: "))
        if num == 0:
            return
        
        print("\nEnter the values for the Nodes: ")
        for data in range(num):
            data = int(input())
            self.append(data)

    def swap_Pair(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        
        p = self.head
        while p != None and p.next != None:
            q = p.next
            p.info, q.info = q.info, p.info
            p = q.next

    


if __name__ == "__main__":
    node_ob = SLL_swapPair()
    node_ob.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes at End.")
        print("3. Swap Pair Wise.")
        print("4. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            node_ob.traversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            node_ob.append(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            node_ob.swap_Pair()
            print("\nSwapping done check the Updated List.")
        elif option == 4:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")