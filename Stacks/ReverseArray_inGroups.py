# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups/0

def ReverseArray(arr, n, k):
    if k > n:
        k = n

    stack = []
    main = [] 
    for i in range(n):
        if len(stack) < k:
            stack.append(arr[i])
        else:
            while len(stack):
                n = len(stack)
                main.append(stack[n-1])
                stack.pop()
            stack.append(arr[i])
    

    while len(stack):
        n = len(stack)
        main.append(stack[n-1])
        stack.pop()

    del stack
    return main

if __name__ == "__main__":
    print("\n")

    arr = [1,2,3,4,5]
    k = 3
    # arr = [10,20,30,40,50,60]
    # k = 2
    n = len(arr)

    res = ReverseArray(arr, n, k)
    print(res)

    print("\n")


