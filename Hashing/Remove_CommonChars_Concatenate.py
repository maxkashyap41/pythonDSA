def RemoveChars(str1, str2):
    hash1 = [0 for k in range(26)]
    hash2 = [0 for k in range(26)]

    for i in range(len(str1)):
        hash1[ord(str1[i])-97] = 1
    
    for i in range(len(str2)):
        hash2[ord(str2[i])-97] = 1
    
    x = ''
    for i in range(len(str1)):
        if hash2[ord(str1[i])-97] != 1:
            x = x+str1[i]
    
    for i in range(len(str2)):
        if hash1[ord(str2[i])-97] != 1:
            x = x+str2[i]
            
    
    if len(x) == 0:
        return -1
    else:
        return x

    
if __name__ == "__main__":
    print("\n")

    # str1 = 'aacdbb'
    # str2 = 'gaffd'
    str1 = 'dkusgfqwniwcbefkpkujoveawvtrmfossimypcxemtgqxnapywaoseq'
    str2 = 'ockiqpwijgu'
    # str1 = 'aabcdpttbc'
    # str2 = 'tbcpabd'

    ans = RemoveChars(str1, str2)
    print(ans)

    print("\n")