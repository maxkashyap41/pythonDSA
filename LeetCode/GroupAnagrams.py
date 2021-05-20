def GroupAnagram(arr, n):
    hashmap = {}
    for i in arr:
        Sort_x = "".join(sorted(i))
        if Sort_x not in hashmap:
            hashmap[Sort_x] = [i]           # hashmap is the dictionary where Sort_x is key and i is the value.
        else:                               # Moreover the hashmap[Sort_x] = [i] means the the value to be inserted 
            hashmap[Sort_x].append(i)       # to that key will be in list format like hashmap = {key1 : [val1, val2], key2 : [val1, val2]}
    #                                       # hashmap[Sort_x] = (i) means in tuple form or hashmap[Sort_x] = {i} means in dict form.
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