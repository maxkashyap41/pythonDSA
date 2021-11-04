# Given a value N, find the number of ways to make change for N cents,
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4.
# For N = 10 and S = {2, 5, 3, 6},
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
# So the output should be 5.

def CoinChange(arr, n, change):
    dp = [[0 for j in range(change+1)] for k in range(n)]
    
    for i in range(n):
        dp[i][0] = 1
    
    for j in range(1, change+1):
        if j % arr[0] == 0:
            dp[0][j] = 1


    for i in range(1, n):
        for j in range(1, change+1):
            if j < arr[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i]]
    
    print(dp)
    return dp[n-1][change]


if __name__ == "__main__":
    print("\n")

    # arr = [2,5,3,6]
    # change = 10
    # arr = [1,2,3]
    # change = 4
    arr = [1,5,6,8]
    change = 11
    n = len(arr)

    result = CoinChange(arr, n, change)
    print("\n", result)

    print("\n")
