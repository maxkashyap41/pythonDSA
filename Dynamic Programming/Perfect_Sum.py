def dpFunc(arr, Sum, ptr, memo):
    key = str(Sum)+':'+str(ptr)
    if key in memo:
        return memo[key]
        
    if Sum == 0:
        return 1
    elif ptr < 0:
        return 0
    elif Sum < arr[ptr]:
        result = dpFunc(arr, Sum, ptr-1, memo)
    else:
        result = dpFunc(arr, Sum-arr[ptr], ptr-1, memo)+dpFunc(arr, Sum, ptr-1, memo)

    print(memo)
    memo[key] = result
    return result



if __name__ == "__main__":
    # arr = [2,3,5,6,8,10]
    # Sum = 10
    # arr = [1,2,3,4,5]
    # Sum = 10
    size = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:size]
    Sum = int(input("Enter the Sum you wanna check for the subsets: "))
    memo = {}

    res = dpFunc(arr, Sum, size-1, memo)

    print("The confirmed subsets present in the Array for the Given Sum: ", res)
    print("\n")