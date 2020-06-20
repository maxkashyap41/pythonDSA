def LongestConsec_Sub(arr):
    arr.sort()
    # print(arr)

    res = list(set(arr))    # to remove duplicacy
    print(res)
    n = len(res)
    maxN = 0
    count = 0
    for i in range(n-1):
        if res[i]+1 == res[i+1]:
            count = count+1
        else:
            maxN = max(maxN, count)
            count = 0
    
    return maxN+1


if __name__ == "__main__":
    print("\n")

    # arr = [36,41,56,35,44,33,34,92,43,32,42]
    # arr = [1,9,3,10,4,20,2]
    n = int(input("Enter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    ans = LongestConsec_Sub(arr)
    print(ans)

    print("\n")
