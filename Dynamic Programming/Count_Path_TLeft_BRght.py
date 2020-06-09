def Count_Path(n, m):
    dp = [[0 for k in range(m)] for l in range(n)]

    for j in range(len(dp[0])):
        dp[0][j] = 1
    
    for i in range(1, n):
        dp[i][0] = 1
    
    # print(dp)

    for i in range(n-1):
        for j in range(m-1):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
    
    print("\nThe DP Board is: ", dp)
    return dp[n-1][m-1]


if __name__ == "__main__":
    # n = 3     # n = 4
    # m = 3     # m = 4

    t = int(input("\nEnter the Number of Test Cases: "))

    while t:
        n, m = map(int, input("\nEnter the Row and Column Size: ").split())

        ans = Count_Path(n, m)

        # Since if output is very large for 32x32 matrix than we shall use the module ans % (10^9 + 7)

        path = ans % 1000000007
        print("Number of path to reach the End: ", path)

        t = t-1

    print("\n")