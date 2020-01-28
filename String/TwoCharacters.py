# input       : beabeefeab
# output      : 5
#               as becoz beabeefeab -> babab so its length is 5

# input       : abaacdabd
# output      : 4
#               as becoz abaacdabd -> bdbd so its length is 4

# explanation : beabeefeab converted to 'babab' and return the length basically remove all the repeating digits and single 
#               non-matching alternating digits like e and f 

def Alternate(string):
    st = list(set(string))
    length = len(st)
    max_len = 0
    for i in range(length):
        for j in range(length):
            res = []
            not_ = bool
            for x in string:
                if x == st[i] or x == st[j]:
                    res.append(x)
            
            for v in range(len(res)-1):
                if res[v] == res[v+1]:
                    not_ = False
                    break
                else:
                    not_ = True
            
            if not_:
                if len(string) == 1: # if string has only one character
                    max_len = 0
                else:
                    max_len = max(max_len, len(res))
    
    return max_len


if __name__ == "__main__":
    string = str(input("\nEnter the String: "))
    length = Alternate(string)
    print("Maximum Length of the converted String is: ", length)
    print("\n")