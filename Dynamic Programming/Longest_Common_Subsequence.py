def CommSubseq(str1, n, str2, m):
    dp = [[0 for j in range(m+1)] for k in range(n+1)]  # list comprehension.

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # max of curr col with prev row and curr row with prev col.

    print(dp)
    return dp[n][m]


if __name__ == "__main__":
    print("\n")
    # str1 = 'ABCDGH'
    # str2 = 'AEDFHR'
    str1 = 'SOLUTIONSADDA'
    str2 = 'ARSNPDMV'
    n = len(str1)
    m = len(str2)

    length = CommSubseq(str1, n, str2, m)
    print(length)

    print("\n")
