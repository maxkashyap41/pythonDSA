def anagram(string):
    maxNo = ord(string[0])
    for i in range(len(string)):
        if maxNo < ord(string[i]):
            maxNo = ord(string[i])
    
    hasht = [0]*(maxNo+1)
    for i in range(len(string)):
        hasht[ord(string[i])] = hasht[ord(string[i])]+1
    
    print(hasht)

    oddCount = 0
    for i in range(len(hasht)):
        if hasht[i] % 2 != 0:
            oddCount = oddCount+1
    
    print(oddCount)
    if oddCount == 0 or oddCount == 1:
        print("Yes") 
    else:
        print("No")
        


if __name__ == "__main__":
    print("\n")
    # string = "geeksogeeks"
    string = "xmddhuaxweosozxjimpcuyisntdbtyjsmmxtiytfcjzqiyzskpueneycadevcpoqelmolftnqudzsftcwqjlujpwpvstlijrvvfhcbutxasqfnuddfoarfwgbqzoyifuekdgnxzlxtbehxjkdzkwfjcgzbualbwplzyzwxmwtpcammkrlxnsgpyhsuhevdvjctkbrwxmlbmzpyrbvgvdyulqqswmysvanfbgdasoeentfgwcnsgnmtfcncqlwlojsrqvuilypzruhowugehuxnylrrynemyxgouazgyohriofelnjsjihkvabunfimeoczobhopogzengpdrkoztavubrhjzvpoaqebxvtnbsuqyjtrvkrpkojmfsxgomwqdbrcwkqzfkpfvlxrvqgfertljqrzfopirjmntcoaodgmofdlvlrbekmnddpitgskpezljnlzttljyqvvbmwfyivbokljsfuikvtvjgueainayiwcushvdewrqkcjpwrbsmwduthwbwxzfvbbnlwspvliforukkyeyujsnspopoqwjrxycururccwqvsdhqjhnvzanqreehapaaofwhznldlcadhjws"
    # string = "elloello"
    anagram(string)
    print("\n")
