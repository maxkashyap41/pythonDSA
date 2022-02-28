# n = 3, X[] = [2 1 6] 
# m = 2, Y[] = [1 5]
# Output: 3
# Explanation: The pairs which follow x^y > y^x are as such: 2^1 > 1^2,  2^5 > 5^2 and 6^1 > 1^6.

# the Exceptions for when x = 0, 1, 2, 3


def getIndex(Y, m, element) -> int:
    l = 0
    r = m-1
    while l < r:
        if Y[l] <= element:
            index = l
            l += 1
        else:
            r -= 1
    #print(index)
    return index


def countPairsFromIndex(index, m, countPairs) -> int:
    if index != -1:
        countPairs += (m-1) - index
    return countPairs


def numberPairs(X, Y, n, m) -> int:
    Y.sort()
    countStore = [0 for _ in range(5)]
    for i in range(m):
        if Y[i] < 5:
            countStore[Y[i]] += 1

    countZeros_Ones = countStore[0] + countStore[1]
    countThrees_Fours = countStore[3] + countStore[4]
    countPairs = 0
    for i in range(n):
        if X[i] == 0:
            continue
        elif X[i] == 1:
            countPairs += countStore[0]
        elif X[i] == 2:
            index = getIndex(Y, m, X[i])
            countPairs = countPairsFromIndex(index, m, countPairs)
            countPairs = (countPairs - countThrees_Fours) + countZeros_Ones 
        elif X[i] == 3:
            index = getIndex(Y, m, X[i])
            countPairs = countPairsFromIndex(index, m, countPairs)
            countPairs += countStore[2] + countZeros_Ones
        else:
            index = getIndex(Y, m, X[i])
            countPairs = countPairsFromIndex(index, m, countPairs)
    
    return countPairs


if __name__ == "__main__":
    print("\n")

    X = [2,1,6]
    Y = [1,5]
    X = [2,3,4,5]
    Y = [1,2,3]
    n = len(X)
    m = len(Y)
    PairNums = numberPairs(X, Y, n , m)
    print(PairNums)

    print("\n")