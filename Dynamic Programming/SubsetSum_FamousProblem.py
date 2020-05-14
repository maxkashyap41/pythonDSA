def dpFunc(arr, Sum, ptr):
    # key = str(Sum)+':'+str(ptr)
    # if key in memo:
    #     return memo[key]

    if Sum == 0:
        return 1
    elif ptr < 0:
        return 0
    elif Sum < arr[ptr]:
        dpFunc(arr, Sum, ptr-1)
    else:
        if dpFunc(arr, Sum-arr[ptr], ptr-1) == 1 or dpFunc(arr, Sum, ptr-1) == 1:
            return True
        
    
    # memo[key] = result
    # return result




if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    total_sum = 0
    for i in range(n):
        total_sum = total_sum+arr[i]

    if total_sum % 2 != 0:
        print("No")
    else:
        Sum = total_sum // 2
        # memo = {}
        if dpFunc(arr, Sum, n-1) == True:
            print("Yes")
        else:
            print("No")

    print("\n")