# Amazon Code
# Input: Arr = [10, 4, 8, 13, 22]
#        k = 2
# Output: 22
# Explanation: Discarding the Maximum Contiguous Memory i.e. 13+22 = 35kb
#              considering 13,22 the two memory slots becoz k=2 and out of all these two slots were having 
#              the largest contiguous memory allocation.
#              And thus returning the remaining memory summation 10+4+8 = 22kb.


def minMemory(arr, n, k) -> int:
    currSum = 0
    maxSum = float('-inf')
    for i in range(k):
        currSum += arr[i]
    
    maxSum = currSum
    for i in range(k, n):
        currSum = currSum + (arr[i] - arr[i-k])
        if maxSum < currSum:
            maxSum = currSum
    
    result = sum(arr) - maxSum
    return result





if __name__ == "__main__":
    print("\n")

    arr = [10,4,8,13,22]
    # arr = arr = [10,4,8,1]
    n = len(arr)
    k = 3
    minLeftMemory = minMemory(arr, n, k)
    print(minLeftMemory)

    print("\n")