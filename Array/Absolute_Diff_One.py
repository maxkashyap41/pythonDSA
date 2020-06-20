# Given an array A of size N.
# Print all the numbers less than K in the array.
# The numbers should be such that 
# the difference between every adjacent digit should be 1.
# Note: Print '-1' if no number if valid.
#
# n, k = 8, 54
# arr = [7,98,56,43,45,23,12,8]
# n, k = 10, 1000
# arr = [87,89,45,235,465,765,123,987,499,655]



def absoluteDiff(arr, n, k):
    res = []
    for i in range(n):
        if arr[i] < k:
            res.append(arr[i])
    
    # print(res)

    main = []
    for i in range(len(res)):
        if res[i] > 9:
            x = str(res[i])
            ls = list(map(int, x))
            for j in range(len(ls)-1):
                if ls[j]-ls[j+1] == 1 or ls[j]-ls[j+1] == -1:
                    ls[j] = 1
            if all(ls[j] == 1 for j in range(len(ls)-1)):
                main.append(res[i])
            
    
    if len(main):
        return 1, main
    else:
        return -1, main


if __name__ == "__main__":
    t = int(input())
    
    while t:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))[:n]
    
        ans, main = absoluteDiff(arr, n, k)
        if ans == 1:
            for i in range(len(main)):
                print(main[i], end = " ")
            print()
        else:
            print(-1)
        
        t = t-1