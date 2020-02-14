class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLL_interY:
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
    

    def append(self, new):
        if self.head == None:
            self.head = new
            return
        
        p = self.head
        while p.next != None:
            p = p.next
        p.next = new
    

def intersectionY(start1, start2):
    p = start1
    while p != None:
        p.info = 0-p.info
        p = p.next
    
    q = start2
    while q.info > 0:
        q = q.next
    q.info = 0-q.info
    
    return q
    


if __name__ == "__main__":
    a = SLL_interY()
    b = SLL_interY()
    print("\nCreate the First List.")
    nodes_a = list(map(int, input("\nEnter the Values: ").split()))
    for i in nodes_a:
        node = Node(i)
        a.append(node)
    print("\nCreate the Second List.")
    nodes_b = list(map(int, input("\nEnter the Values: ").split()))
    for i in nodes_b:
        node = Node(i)
        b.append(node)

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Intersection of Y 'famous GFG question !. PLease TRY....")
        print("3. Quit.")

        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            print("\nFirst List: ", end = " ")
            a.traversal()
            print("\nSecond List: ", end = " ")
            b.traversal()
        elif option == 2:
            print("\nCreate the Common List of Intersection.")
            common = list(map(int, input("\nEnter the Values: ").split()))
            for i in range(len(common)):
                node = Node(common[i])
                a.append(node)
                if i == 0:
                    b.append(node)

            if intersectionY(a.head, b.head) == -1:
                print("\n")
                print(-1)
            else:
                print("\n")
                print(intersectionY(a.head, b.head).info)
        elif option == 3:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
        
    print("\n")