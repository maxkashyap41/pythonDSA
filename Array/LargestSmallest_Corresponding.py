# sort the largest number into descending and smallest number in ascending.
# Example: 37 12 33 9 43 19 20 -> 43 9 37 12 33 19 20


def LargestSmallest(arr, n):
    sort_arr = sorted(arr)
    length = len(sort_arr)
    mid = length // 2
    res = [-1]*n
    
    # for largest
    x = 0
    for i in range(n-1, mid-1, -1):
        res[x] = sort_arr[i]
        x = x+2

    # for smallest
    x = 1
    for i in range(0, mid, 1):
        res[x] = sort_arr[i]
        x = x+2
    
    return res



def LargeSmall2(arr, n):
    arr.sort()
    new_arr = [-1 for _ in range(n)]
    print(new_arr)


    mid = n // 2
    j = 0
    for i in range(n-1, mid-1, -1):
        new_arr[j] = arr[i]
        j += 2
    
    j = 1
    for i in range(0, mid, 1):
        new_arr[j] = arr[i]
        j += 2
    
    print(new_arr)



if __name__ == "__main__":
    # print("\n")
    # arr = [5, 10, 15, 2, 3, 9, 7, 8, 11]
    # n = len(arr)
    # LargestSmallest(arr, n)
    # print("\n")


    print("\n")
    # arr = [37, 12, 33, 9, 43, 19, 20]
    arr = [5, 10, 15, 2, 3, 9, 7, 8, 11]
    n = len(arr)
    LargeSmall2(arr, n)
    print("\n")

    # n = int(input("\nEnter the Array Size: "))
    # arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    # res = LargestSmallest(arr, n)
    # print("\nSorted List: ", end = " ")
    # for i in range(len(res)):
    #     print(res[i], end = " ")
    print("\n")


