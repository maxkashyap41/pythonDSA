def GroupAnagram(arr, n):
    hashmap = {}
    for i in arr:
        Sort_x = "".join(sorted(i))
        if Sort_x not in hashmap:
            hashmap[Sort_x] = [i]
        else:
            hashmap[Sort_x].append(i)
    
    # print(hashmap)
    result = []
    for i in hashmap.values():
        result.append(i)
    
    return result




if __name__ == "__main__":
    print("\n")
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    n = len(arr)
    
    res = GroupAnagram(arr, n)
    print(res)
    
    print("\n")