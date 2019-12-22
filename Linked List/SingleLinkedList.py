class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head == None:
            print("\nList is Empty !")
            return
        else:
            print("\nList is :", end = " ")
            p = self.head
            while p != None:
                print(p.info, end = " ")
                p = p.next
            print("\n")

    def count_nodes(self):
        count = 0
        p = self.head
        while p != None:
            count = count+1
            p = p.next
        print("\nThe Number of Nodes are: ", count)
    
    def search(self, x):
        pos = 1
        p = self.head
        while p != None:
            if x == pos:
                print(x, "\n is found at the position ", pos)
                return True
            pos = pos+1
            p = p.next

        print("\n", x, " not found in the list !")
        return False

    def insertion_at_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insertion_at_end(self, data):
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
        print("\nEnter the value for the Nodes: ")
        for data in range(num):
            data = int(input())
            self.insertion_at_end(data)
    
    def insertion_in_between(self, x, data):
        if self.head == None:
            print("\nList Empty !")
            return
        
        new = Node(data)
        p = self.head
        while p.next != None:
            if p.info == x:
                break
            p = p.next
        if x == None:
            print(x, " not found !")
            return
        else:
            new.next = p.next
            p.next = new


# Menu Driven Function

if __name__ == "__main__":
    list_ob = SingleLinkedList()
    list_ob.create_list()

    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display List.")
        print("2. Number of Nodes.")
        print("3. Search for an Element.")
        print("4. Insert at Beginning of the List.")
        print("5. Insert at Ending of the List.")
        print("6. Insert in between the Nodes.")
        print("7. Quit.")

        option = int(input("\nEnter ur Choice: "))

        if option == 1:
            list_ob.traversal()
        elif option == 2:
            list_ob.count_nodes()
        elif option == 3:
            element = int(input("\nEnter the Number you wanna a find: "))
            list_ob.search(element)
        elif option == 4:
            value1 = int(input("\nEnter the value to insert at Begin: "))
            list_ob.insertion_at_begin(value1)
        elif option == 5:
            value1 = int(input("\nEnter the value to insert at End: "))
            list_ob.insertion_at_end(value1)
        elif option == 6:
            x = int(input("\nEnter the Node behind which new value to be inserted: "))
            data = int(input("\nEnter the new data to be inserted: "))
            list_ob.insertion_in_between(x, data)
        elif option == 7:
            break
        else:
            print("\nWrong Input no where else to found !")
    
    print("\n")
        