def sort(arr, n):
    # arr.sort()
    # return arr

    c0 = 0
    c1 = 0
    c2 = 0
    for i in range(n):
        if arr[i] == 0:
            c0 = c0+1
        if arr[i] == 1:
            c1 = c1+1
        if arr[i] == 2:
            c2 = c2+1
    
    for i in range(c0):
        arr[i] = 0
    for i in range(c0, c0+c1):
        arr[i] = 1
    for i in range(c0+c1, c0+c1+c2):
        arr[i] = 2
    
    return arr



if __name__ == "__main__":
    print("\n")

    # arr = [0, 2, 1, 2, 0]
    arr = [0, 1, 0]
    n = len(arr)

    new_arr = sort(arr, n)

    print(new_arr)

    print("\n")