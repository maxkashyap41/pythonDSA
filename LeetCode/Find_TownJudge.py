# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.





def LeetCode(arr, n):
    if n == 1:
        print(1)
    else:    
        hashTrst = [0]*(n+1)
        hashTrstBy = [0]*(n+1)
        for i in arr:
            for j in range(len(i)-1):
                hashTrst[i[j]] = hashTrst[i[j]]+1
                hashTrstBy[i[j+1]] = hashTrstBy[i[j+1]]+1
    
        print(hashTrst)
        print(hashTrstBy)
    
        j = 1
        res = -1
        for i in range(1, len(hashTrst)):
            if hashTrst[i] == 0 and hashTrstBy[j] == n-1:
                res = hashTrstBy[j]
            j = j+1
    
        if res == -1:
            print(res)
        else:
            index = hashTrstBy.index(res)
            print(index)



if __name__ == "__main__":
    print("\n")
    arr = [[1,3], [1,4], [2,3], [2,4], [4,3]]
    n = 4
    # arr = [[1,3], [2,3]]
    # n = 3
    # arr = [[1,3], [2,3], [3,1]]
    # n = 3
    # arr = [[1,2], [2,3]]
    # n = 3
    # arr = []
    # n = 1

    LeetCode(arr, n)

    print("\n")