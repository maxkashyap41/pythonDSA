# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.



# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


def LeetCode(arr, n):
    pass

if __name__ == "__main__":
    print("\n")
    # arr = [1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0]
    # arr = [0,1,0]
    # arr = [1,0,0,1,0,1,1]
    # arr = [1,0,1,1,1,0,0]
    arr = [0,1]
    n = len(arr)
    print("Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")

    # res = LeetCode(arr, n)
    # print("\nMaximum Length of the Contagious SubArray: ", res)
    print("\n")

