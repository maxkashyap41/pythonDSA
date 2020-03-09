# input       : 1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65
#
# output      : 4
# explanation : to find the element with atleast occurring once 
#               its algo for DNC will be 
#               
#               if mid is even then
#               we will look for 
#               if mid ele == mid+1 ele
#                   use recursion to call function starting mid+2 to high
#               else
#                   use recursion to call function starting low to mid
#               
#               but if mid is odd then
#               we look for 
#               if mid ele == mid-1 ele
#                   use recursion to call function starting mid+1 to high
#               else
#                   use recursion to call function starting low to mid-1
#               




def elementOnce(arr, low, high):
    if low > high:
        return None
    
    if low == high:
        print(arr[low])
        return
    
    mid = low + (high-low)//2
    # print(mid)

    if mid % 2 == 0:
        if arr[mid] == arr[mid+1]:
            elementOnce(arr, mid+2, high)
        else:
            elementOnce(arr, low, mid)
    else:
        if arr[mid] == arr[mid-1]:
            elementOnce(arr, mid+1, high)
        else:
            elementOnce(arr, low, mid-1)

if __name__ == "__main__":
    print("\n")
    arr = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
    n = len(arr)

    print("Element that appeared once:~ ", end = " ")
    elementOnce(arr, 0, n-1)
    
    print("\n")

