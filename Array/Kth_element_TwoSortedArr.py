def kth_element(arr, brr, k):
    for i in range(len(brr)):
        arr.append(brr[i])
    
    arr.sort()
    print(arr)
    
    for i in range(len(arr)):
        if i+1 == k:
            return arr[i]



if __name__ == "__main__":
    print("\n")
    arr = [2, 3, 6, 7, 9]
    brr = [1, 4, 8, 10]
    k = 5

    element = kth_element(arr, brr, k)
    print("Print Element is :~ ", element)

    print("\n")