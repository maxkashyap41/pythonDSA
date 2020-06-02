def MinimumJumps(arr, n):
    if arr[0] == 0:
        return -1
    jumps = [None]*n
    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if i <= j+arr[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j]+1)
                break
    
    print("\n", jumps)
    if jumps[n-1] == float('inf'):
        return -1
    return jumps[n-1]





if __name__ == "__main__":
    print("\n")
    # arr = [2,3,1,1,2,4,2,0,1,1]
    # arr = [2,1,0,3]
    arr = [2,3,1,1,4,2,0,1,1]
    # arr = [1,3,5,8,9,2,6,7,6,8,9]
    n = len(arr)
    
    print("Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")
    
    minJumps = MinimumJumps(arr, n)
    print("\nMinimum Jumps: ", minJumps)
    print("\n")