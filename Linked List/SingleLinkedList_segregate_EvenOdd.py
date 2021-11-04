class Node:
    def __init__(self, value):
        self.info = value
        self.next = None


class SLLseg_ev_od:
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
    
    def createlist(self, num):        
        print("\nEnter the values for the Nodes: ", end = " ")
        arr = list(map(int, input().split()))[:num]
        for i in range(num):
            self.append(arr[i])
    
def segregate(start):
    even = []
    odd = []
    p = start
    while p != None:
        if p.info % 2 == 0:
            even.append(p.info)
        else:
            odd.append(p.info)
        p = p.next
        
    elen = len(even)
    olen = len(odd)

    segobj = SLLseg_ev_od()    
    for i in range(elen):
        segobj.append(even[i])
        
    for i in range(olen):
        segobj.append(odd[i])
    
    return segobj

        


if __name__ == "__main__":
    t = int(input())

    while t:
        obj = SLLseg_ev_od()

        num = int(input("\nEnter the Number of Nodes of u want:  "))
        if num == 0:
            print(-1)
        
        obj.createlist(num)
        obj.traversal()

        print("\n----- | Resultant List | -----")
        segob = segregate(obj.head)
        segob.traversal()
        

        t = t-1
    
    print("\n")
        