# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k/0

def MaxSumOfSubArr(arr, n, k):
    currSum = 0
    for i in range(k):
        currSum += arr[i]
    
    maxSum = float('-inf')
    for i in range(k, n):
        currSum += arr[i] - arr[i-k]
        maxSum = max(maxSum, currSum)
    
    return maxSum


if __name__ == "__main__":
    print("\n")

    arr = [100,200,300,400]
    k = 2
    n = len(arr)

    # arr = [1,4,2,10,23,3,1,0,20]
    # k = 4
    # n = len(arr)

    maxSum = MaxSumOfSubArr(arr, n , k)
    print(maxSum)

    print("\n")

