# Given an array nums, write a function to move all 0's to 
# the end of it while maintaining the relative order of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


def LeetCode(arr, n):
    new_ls = [None]*n
    j = 0
    for i in range(n):
        if arr[i] != 0:
            new_ls[j] = arr[i]
            j = j+1
    
    arr.clear()
    print("Original Deleted Array: ", arr)
    
    for i in range(n):
        if new_ls[i] == None:
            new_ls[i] = 0
    
    for i in range(len(new_ls)):
        arr.append(new_ls[i])

    del new_ls
    return arr


if __name__ == "__main__":
    print("\n")
    arr = [0,1,0,3,12]
    n = len(arr)
    print("Array Elements are: ", arr)

    res = LeetCode(arr, n)
    print("\nResultant Array is: ", res)

    print("\n")