# input       : beabeefeab
# output      : 5
#               as becoz beabeefeab -> babab so its length is 5

# input       : abaacdabd
# output      : 4
#               as becoz abaacdabd -> bdbd so its length is 4

# explanation : beabeefeab converted to 'babab' and return the length basically remove all the repeating digits and single 
#               non-matching alternating digits like e and f

def TwoCharacters(string):
    uniqueStringList = list(set(string))
    length = len(uniqueStringList)
    resStringList = []
    max_len = 0
    for i in range(length):
        for j in range(length):
            comparedList = []
            not_ = bool
            for x in string:
                if x == uniqueStringList[i] or x == uniqueStringList[j]:
                    comparedList.append(x)
            
            for v in range(len(comparedList)-1):
                if comparedList[v] == comparedList[v+1]:
                    not_ = False
                    break
                else:
                    not_ = True
            
            if not_ == True:    # also can be written as if not_: which means it is true
                if len(string) == 1:
                    max_len = 0
                else:
                    max_len = max(max_len, len(comparedList))

                    # storing the list of reduced string characters
                    if len(comparedList) == max_len:
                        resStringList = comparedList
    
    # converting list to string
    xString = ''.join(resStringList)
    
    return max_len, xString


if __name__ == "__main__":
    string = str(input("\nEnter the String: "))

    size, reducedString = TwoCharacters(string)

    print("\nReduced Size: ", size)
    print("Reduced String: ", reducedString)
    print("\n")