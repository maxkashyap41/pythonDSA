def testFunc(hashmap):
    result = []
    for i in hashmap.values():
        for j in i:
            result.append(j)
    
    print(result)

    maxN = result[0]
    for i in range(len(result)):
        maxN = max(maxN, result[i])
    
    hashT = [0]*(maxN+1)
    for i in range(len(result)):
        hashT[result[i]] = hashT[result[i]]+1
    
    print(hashT)

    maxHT = hashT[0]
    for i in range(len(hashT)):
        maxHT = max(maxHT, hashT[i])
    
    res = hashT.index(maxHT)
    print(res)


if __name__ == "__main__":
    print("\n")
    hashmap = {1:[3, 4], 2:[3,4], 4:[3]}

    testFunc(hashmap)
    print("\n")
