def LeetCode(arr, n):
    hashmap = {}

    for i in arr:
        for j in range(len(i)-1):
            if i[j] not in hashmap:
                hashmap[i[j]] = [i[j+1]]
            else:
                hashmap[i[j]].append(i[j+1])
    
    print(hashmap)

    result = []
    for values in hashmap.values():
        for j in values:
            result.append(j)
    
    print(result)




if __name__ == "__main__":
    print("\n")
    arr = [[1,3], [1,4], [2,3], [2,4], [4,3]]
    n = len(arr)

    LeetCode(arr, n)

    print("\n")