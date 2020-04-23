class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class LeetCode:
    def __init__(self):
        self.head = None
    

    def traversal(self):
        if self.head == None:
            print("\nList is Empty!")
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
    

    def createlist(self):
        num = int(input("\nEnter the Number of Nodes: "))

        if num == 0:
            return
        
        print("\nEnter the values for the Nodes: ")
        for i in range(num):
            i = int(input())
            self.append(i)
    

    def midValue(self):
        p = self.head
        count = 1
        while p.next != None:
            p = p.next
            count = count+1
        
        # print(count)
        
        if count == 1:
            return p.info
        
        if count == 2:
            while p.next != None:
                p = p.next
            return p.info

        mid = (count // 2) + 1

        c = 1
        p = self.head
        while p.next != None:
            if c == mid:
                return p.info
            p = p.next
            c = c+1
            




if __name__ == "__main__":
    objct = LeetCode()
    objct.createlist()

    print("\n**************************** | SINGLE LINKED LIST | ****************************")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append Node at the End of the List.")
        print("3. Print the MidNode of the List.")
        print("4. Quit.")

        option = int(input("\nEnter your Option: "))

        if option == 1:
            objct.traversal()
        elif option == 2:
            data = int(input("\nEnter the Value you wanna see: "))
            objct.append(data)
            print("\nInsertion done check the updated List.")
        elif option == 3:
            res = objct.midValue()
            print(res)
        elif option == 4:
            print("\nThank You for your time.")
            break
        else:
            print("\nWrong Input....Try again!")
    
    print("\n")
        