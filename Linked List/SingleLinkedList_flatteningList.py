class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
        self.down = None

def traversal(node):     
    print("\nList is: ", end = " ")
    while node != None:
        print(node.info, end = " ")
        node = node.down
    print("\n")


def merge(p, q):
    if p == None:
        return q
    if q == None:
        return p

    if p.info < q.info:
        ptr = p
        ptr.down = merge(p.down, q)
    else:
        ptr = q
        ptr.down = merge(p, q.down)

    return ptr


def flatten(head):
    if head == None or head.next == None:
        return head

    return merge(head, flatten(head.next))



if __name__ == "__main__":
    head = None
    N = int(input("\nEnter the Size: "))
    arr = []
    arr = [int(x) for x in input().split()]
    temp = None
    tempB = None
    pre = None
    preB = None

    flag = 1
    flag1 = 1
    listto = [int(x) for x in input().split()]
    j = 0
    for i in range(N):
        m = arr[i]
        m = m-1
        a1 = listto[j]
        j = j+1
        temp = Node(a1)
        if flag is 1:
            head = temp
            pre = temp
            flag = 0
            flag1 = 1
        else:
            pre.next = temp
            pre = temp
            flag1 = 1

        for j in range(m):
            a = listto[j]
            j = j+1
            tempB = Node(a)
            if flag1 is 1:
                temp.down = tempB
                preB = tempB
                flag1 = 0
            else:
                preB.down = tempB
                preB = tempB
    root = flatten(head)
    traversal(root)

    print("\n") 