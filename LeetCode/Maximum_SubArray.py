# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.


# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def kadaneAlgo(arr, n):
    Sum = arr[0]
    maxSum = arr[0]
    for i in range(1, n):
        Sum = max(arr[i], Sum+arr[i])
        if maxSum < Sum:
            maxSum = Sum
    
    return maxSum


if __name__ == "__main__":
    print("\n")
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    n = len(arr)
    print("Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")
    
    res = kadaneAlgo(arr, n)
    print("\nMaximum SubArray Sum: ", res)
    print("\n")