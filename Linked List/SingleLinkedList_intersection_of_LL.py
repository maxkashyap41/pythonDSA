class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLintersection:
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
    

    def intersectionList(self, list2):
        p = self.head
        q = list2.head
        arr = []
        while p != None:
            arr.append(p.info)
            p = p.next
        
        while q != None:
            arr.append(q.info)
            q = q.next
        
        arr.sort()
        intersectionArr = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    intersectionArr.append(arr[j])
        return intersectionArr



if __name__ == "__main__":
    a = SLLintersection()
    b = SLLintersection()

    a.create_list()
    b.create_list()


    print("\n-------------------- Single Linked List --------------------\n")

    while True:
        print("\n\n1. Display the List.")
        print("2. Append the Nodes.")
        print("3. Intersections of 2 Lists.")
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
            print("\nUnion of List Done check the Updated List ||BELOW||.")
            new_arr = a.intersectionList(b)
            print("\nElements are: ", end = " ")
            for i in range(len(new_arr)):
                print(new_arr[i], end = " ")
            print("\n")
        elif option == 4:
            print("\nThank You for ur time !")
            break
        else:
            print("\nWrong option try again !")
    
    print("\n")