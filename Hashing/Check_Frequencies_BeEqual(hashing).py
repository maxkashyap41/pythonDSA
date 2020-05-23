def frequency(string):
    hashmap = {}
    for item in string:
        if item not in hashmap:
            hashmap[item] = 1
        else:
            hashmap[item] = hashmap[item]+1
    
    print(hashmap)

    res_ls = []
    for values in hashmap.values():
        res_ls.append(values)
    
    print(res_ls)

    maxN = max(res_ls)
    if maxN == 1:
        return 1

    hashT = [0]*(maxN+1)

    for i in range(len(res_ls)):
        hashT[res_ls[i]] = hashT[res_ls[i]]+1
    
    print(hashT)
    
    if len(hashT) == 3:
        for i in hashT:
            if i == 1:
                return 1

    return 0



    
        

if __name__ == "__main__":
    print("\n")
    # string = 'xyz'
    # string = 'xxxxyyzz'
    # string = 'xyyz'
    # string = 'evjxpnqgmvfjl'
    string = 'ehuuroaidj'
    # string = 'cceea'
    # string = 'lptpgwgjrwlgtdhdui'

    res = frequency(string)
    print(res)


    print("\n")
