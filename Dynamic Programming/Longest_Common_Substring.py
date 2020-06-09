def Substring(str1, str2, n, m):
    dp = [[0 for k in range(m+1)] for l in range(n+1)]

    maxN = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                
                if maxN < dp[i][j]:
                    maxN = dp[i][j]
                

    # print(dp)
    flag = -1
    res = maxN
    x = ''
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            if dp[i][j] == maxN:
                x = x+str2[j-1]
                maxN = maxN-1
            if maxN < 1:
                flag = 1
                break
        if flag == 1:
            break
    
    x = x[::-1]         # it got started from the backside !
    print("The Common Substring:       ", x)
    return res



if __name__ == "__main__":
    print("\n")

    # str1 = 'ABCDGH'
    # str2 = 'ACDGHR'
    str1 = 'ABC'
    str2 = 'AC'

    n = len(str1)
    m = len(str2)

    ans = Substring(str1, str2, n, m)
    print("Length of Common Substring: ", ans)

    print("\n")