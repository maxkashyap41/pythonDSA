# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k/0


def SumSubArr(arr, n, k):
    Sum = 0
    j = 0
    while j < k:
        Sum = Sum+arr[j]
        j = j+1
    
    maxSum = Sum
    i = 0
    while j < n:
        Sum = Sum + (arr[j]-arr[i])
        maxSum = max(maxSum, Sum)
        j = j+1
        i = i+1
    
    return maxSum


if __name__ == "__main__":
    print("\n")

    # arr = [100,200,300,400]
    # k = 2
    arr = [1,4,2,10,23,3,1,0,20]
    k = 4
    n = len(arr)

    maxSum = SumSubArr(arr, n , k)
    print(maxSum)

    print("\n")

