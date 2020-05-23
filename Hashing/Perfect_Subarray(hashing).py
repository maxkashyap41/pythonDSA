# In sample case #2, there are three perfect subarrays:
# [9], whose total sum is 32.
# [1], whose total sum is 12.
# [30 30 9 1 30], whose total sum is 102.

# In sample case #3, there are nine perfect subarrays:
# [4], whose total sum is 22.
# [4 0], whose total sum is 22.
# [4 0 0], whose total sum is 22.
# [0], whose total sum is 02.
# [0 0], whose total sum is 02.
# [0 0 16], whose total sum is 42.
# [0], whose total sum is 02.
# [0 16], whose total sum is 42.
# [16], whose total sum is 42.


def Kickstart(arr, n):
    Sum = 0
    for i in range(n):
        Sum = Sum+abs(arr[i])
    
    cnt = [0]*(2*Sum+1)
    cnt[Sum] = cnt[Sum]+1

    pref = ans = 0
    for i in range(n):
        # print(ans)
        pref = pref+arr[i]
        j = 0
        while j*j <=Sum+pref:
            ans = ans+cnt[Sum+pref - j*j]
            j = j+1
        
        cnt[Sum+pref] = cnt[Sum+pref]+1
    

    return ans



if __name__ == "__main__":
    print("\n")
    # arr = [30,30,9,1,30]
    # arr = [2,2,6]
    # arr = [4,0,0,16]
    # n = len(arr)

    n = int(input("\nSize of the Array: "))
    arr = list(map(int, input("Array Elements: ").split()))[:n]

    res = Kickstart(arr, n)
    print("\nResult: ", res)

    print("\n")