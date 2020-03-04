# input       : 1, 2, 3, 7, 5 
#               Sum ~ 12
# output      : Positions 2 and 4
# explanation : basically runs on the sliding window protocol like i and j will at initial 0, then j will be incremented 
#               till the t_sum greater than Sum if t_sum > Sum than we will substract the t_sum with arr[i] and 
#               increment i till t_sum < Sum.
#               Now if we found the t_sum == Sum then return i and j positions or else continue by incrementing j till
#               the t_sum becomes greater than Sum so that arr[i] gets substarcted till we find the positions for the
#               reqd Sum. 



def subArraySum(arr, n, m):
    # *************** BRUTE FORCE ***************
    #
    # for i in range(n):
    #     _sum = arr[i]
    #     for j in range(i+1, n):
    #         _sum = _sum+arr[j]

    #         if _sum == m:
    #             return i, j
        
    # return -1
    #
    # *******************************************


    i = 0
    j = 0
    t_sum = 0
    while j < n:
        t_sum = t_sum+arr[j]
        
        while t_sum > m:
            t_sum = t_sum-arr[i]
            i = i+1
        
        if t_sum == m:
            return i, j
        else:
            j = j+1
            continue
    
    return -1
        


if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    m = int(input("Enter the Sum you wanna find: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    
    if subArraySum(arr, n, m) == -1:
        print("-1")
    else:
        pos1, pos2 = subArraySum(arr, n, m)
        print("Position at: ", pos1+1, pos2+1)
    
    print("\n")