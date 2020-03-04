# input       : 1, 4, 5, -7, -8, 2, 3
#               
# output      : 10
# explanation : Print the maximum sum of the contiguous sub-array.
#               
#               



def kadane(arr, n):
    # *************** BRUTE FORCE ***************
    #
    # tmax = arr[0]
    
    # for i in range(n):
    #     res = arr[i]
    #     for j in range(i+1, n):
    #         res = res+arr[j]
    #         if tmax < res:
    #             tmax = res
    
    # return tmax
    #
    # *******************************************

    res = arr[0]
    t_max = arr[0]
    for i in range(1, n):
        res = max(arr[i], res+arr[i])
        if t_max < res:
            t_max = res

    return t_max

if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    
    answer = kadane(arr, n)

    print("Sum is: ", answer)
    
    print("\n")