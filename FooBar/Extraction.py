def extraction(numString, string):
    hashmap = {}
    extractList = []
    i = 0
    while i < len(numString):
        x = ""
        count = 0
        while count < 6:
            x = x+numString[i]
            i = i+1
            count = count+1
        extractList.append(x)
        continue

    # print(extractList)

    j = 0
    for i in string:
        if i not in hashmap:
            hashmap[i] = extractList[j]
            j = j+1
    
    print(hashmap)


if __name__ == "__main__":
    print("\n")
    numString = "000001110000111010100000010100111000111000100010"
    string = "Braille"
    # numString = "100100101010100110100010"
    # string = "code"

    extraction(numString, string)

    print("\n")
        