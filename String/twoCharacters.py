# input       : beabeefeab
# output      : 5
#               as becoz beabeefeab -> babab so its length is 5

# input       : abaacdabd
# output      : 4
#               as becoz abaacdabd -> bdbd so its length is 4

# explanation : beabeefeab converted to 'babab' and return the length basically remove all the repeating digits and single 
#               non-matching alternating digits like e and f

def TwoCharacters(string):
    extracted_string = list(set(string))
    exlen = len(extracted_string)
    resStringList = []
    maxlen = 0
    for i in range(exlen):
        for j in range(exlen):
            compared_list = []
            bool_ = False
            for x in string:
                if x == extracted_string[i] or x == extracted_string[j]:
                    compared_list.append(x)
            
            complen = len(compared_list)
            for v in range(complen-1):
                if compared_list[v] == compared_list[v+1]:
                    bool_ = True
                    break
            
            if bool_ == False:    # also can be written as if not_: which means it is true
                if len(string) == 1:
                    maxlen = 0
                else:
                    maxlen = max(maxlen, complen)

                    # storing the list of reduced string characters
                    if complen == maxlen:
                        resStringList = compared_list
    
    # converting list to string
    xString = ''.join(resStringList)
    
    return maxlen, xString


if __name__ == "__main__":
    string = str(input("\nEnter the String: "))

    size, reducedString = TwoCharacters(string)

    print("\nReduced Size: ", size)
    print("Reduced String: ", reducedString)
    print("\n")