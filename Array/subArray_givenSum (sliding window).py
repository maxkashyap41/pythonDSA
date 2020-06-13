# input       : 1, 2, 3, 7, 5 
#               Sum ~ 12
# output      : Positions 2 and 4
# explanation : basically runs on the sliding window protocol like i and j will at initial 0, then j will be incremented 
#               till the t_sum greater than Sum if t_sum > Sum than we will substract the t_sum with arr[i] and 
#               increment i till t_sum < Sum.
#               Now if we found the t_sum == Sum then return i and j positions or else continue by incrementing j till
#               the t_sum becomes greater than Sum so that arr[i] gets substarcted till we find the positions for the
#               reqd Sum.

def subArray(arr, n, k):
    Sum = 0
    i = j = 0
    while j < n:
        Sum = Sum+arr[j]

        while Sum > k:
            Sum = Sum-arr[i]
            i = i+1
        if Sum == k:
            return i,j
        else:
            j= j+1
    
    return -1



if __name__ == "__main__":
    # arr = [1,2,3,7,5]
    # k = 12
    # arr = [1,2,3,4,5, 6,7,8,9,10]
    # k = 15
    # n = len(arr)

    n, k = map(int, input("\nEnter the Size and Sum 'k': ").split())
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    
    if subArray(arr, n, k) == -1:
        print("-1")
    else:
        start, end = subArray(arr, n, k)
        print("Position at: ", start+1, end+1)

    print("\n")