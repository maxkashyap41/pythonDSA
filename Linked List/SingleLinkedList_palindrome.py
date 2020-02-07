class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLpalindrome:
    def __init__(self):
        self.head = None
    
    
    def tarversal(self):
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
    

    def creatlist(self):
        num = int(input("\nEnter the Number of Nodes: "))
        if num == 0:
            return
        
        print("\nEnter the value for the Nodes:")
        for i in range(num):
            i = int(input())
            self.append(i)
    

    def Palindrome(self):
        count = 0
        p = self.head
        while p != None:
            p = p.next
            count = count+1
        print("\nNodes are ->", count)

        list1 = []
        list2 = []
        p = self.head
        if count % 2 != 0:
            mid = (count // 2)
            for i in range(mid):
                list1.append(p.info)
                p = p.next
            del i
            q = p.next
            while q != None:
                list2.append(q.info)
                q = q.next
        else:
            mid = (count // 2)
            for i in range(mid):
                list1.append(p.info)
                p = p.next
            q = p
            while q != None:
                list2.append(q.info)
                q = q.next
        
        # print(list1)
        list2.reverse()
        # print(list2)
        print("\nIf ans -> 1 then is PALINDROME.")
        print("********** OR **********")
        print("If ans -> 0 then is not PALINDROME.")
        if list1 == list2:
            print("\nResult -> 1")
        else:
            print("\nResult -> 0")





if __name__ == "__main__":
    objct = SLLpalindrome()
    objct.creatlist()

    print("\n-------------------- Single Linked List --------------------\n")

    while(True):
        print("\n\n1. Display the List.")
        print("2. Append Nodes.")
        print("3. Is the SLL is palindrome or not !")
        print("4. Quit.")
        
        option = int(input("\nEnter the preferred option: "))

        if option == 1:
            objct.tarversal()
        elif option == 2:
            data = int(input("\nEnter the new value: "))
            objct.append(data)
            print("\nInsertion done check the Updated List.")
        elif option == 3:
            objct.Palindrome()
        elif option == 4:
            print("\nThank You for your time !")
            break
        else:
            print("\nWrong input please try again !")
    
    print("\n")