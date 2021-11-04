# This problem basically tact’s to replace 
# two strings characters alike to each other.


def editDistance(str1, n, str2, m):
    dp = [[0 for j in range(m+1)] for k in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i
    
    for j in range(m+1):
        dp[0][j] = j

    print(dp)

    minN = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                minN = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                dp[i][j] = minN+1
                minN = 0
    
    print(dp)
    return dp[n][m]


if __name__ == "__main__":
    print("\n")

    # str1 = 'sitting'
    # str2 = 'kitten'
    str1 = 'geek'
    str2 = 'gesek'

    n = len(str1)
    m = len(str2)

    edits = editDistance(str1, n, str2, m)
    print(edits)

    print("\n")