def arrayZigZag(arr, n):
    flag = 0 # to determine the zigzag !
    i = 0
    while i < n-1:
        if flag == 0:
            if arr[i] < arr[i+1]:
                i = i+1
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                i = i+1
        elif flag == 1:
            if arr[i] > arr[i+1]:
                i = i+1
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                i = i+1
        
        flag = not flag
    
    return arr


if __name__ == "__main__":
    print("\n")
    # arr = [4, 3, 7, 8, 6, 2, 1]
    arr = [1, 4, 3, 2]
    n = len(arr)

    new_arr = arrayZigZag(arr, n)
    print("The ZigZag pattern of the Array: ", new_arr)

    print("\n")
    
