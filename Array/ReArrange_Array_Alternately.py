# arr[] = {1,2,3,4,5,6}
# Output: 6 1 5 2 4 3
# Explanation: Max element = 6, min = 1, 
# second max = 5, second min = 2, and 
# so on... Modified array is : 6 1 5 2 4 3.
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).



def ReArrange_Array(arr, n):
    pass


if __name__ == "__main__":
    print("\n")

    arr = [1,2,3,4,5,6]
    n = len(arr)

    resultantArray = ReArrange_Array(arr, n)
    print(resultantArray)

    # t = int(input("\nEnter the Testcases: "))
    
    # while t:
    #     n = int(input("\nEnter the Array Size: "))
    #     arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    #     res = ReArrange_Array(arr, n)
    #     print("After ReArrangement of the Array: ")
    #     for i in range(n):
    #         print(res[i], end = " ")

    #     print()
    #     t = t-1

    print("\n")