# https://practice.geeksforgeeks.org/problems/subarray-range-with-given-sum/0
# Given an unsorted array arr[] of N integers and a sum.
# The task is to count the number of subarrays which add to a given number.
# i/p- [5,5,12,2,8] sum ~ 10    o/p- 2 (two subsets of array available)

def subArray(arr, n, t_sum):
    hashmap = {}
    res = []
    count = 0
    Sum = 0
    for i in range(n):        
        Sum = Sum+arr[i]

        if Sum == t_sum:
            count = count+1
        if Sum-t_sum in hashmap:
            for item in hashmap[Sum-t_sum]:
                res.append(item)

        if Sum not in hashmap:
            hashmap[Sum] = [i]
        else:
            hashmap[Sum].append(i)        

    # print(res)
    # print(hashmap)
    count = count+len(res)
    return count


if __name__ == "__main__":
    print("\n")
    # arr = [10,2,-2,-20,10]      # arr = [1,4,20,3,10,5]
    # t_sum = -10                # t_sum = 33
    # arr = [5,5,12,2,8]
    # t_sum = 10
    n = int(input("Enter the Size: "))
    arr = list(map(int, input("Enter Array Elements: ").split()))[:n]
    t_sum = int(input("Enter the Sum: "))

    count = subArray(arr, n, t_sum)
    print(count)

    print("\n")