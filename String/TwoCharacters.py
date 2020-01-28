# step 1 -> Take string input.
# step 2 -> Remove all the dups from string and store it in list named 'st' using set().
# step 3 -> start 2 loops in the new list that is 'st'
# step 4 -> make another new list 'res' by comparing the string characters and st list 
#           elements like if a is present in string and 'st' list then store that 
#           in 'res' list.
# step 5 -> So now in the 'res' list we see if there is any same corresponding element 
#           is present or not if present we shall not validate its length and return 
#           false and if no corresponding element present than we return the length 
#           of that 'res' list.
# Note:     The 'res' which willl formed will be inside two loops as the comparison 
#           between the string and 'st' list will be quite long.

def Alternate(string):
    st = list(set(string))
    length = len(st)
    max_len = 0
    for i in range(length):
        for j in range(length):
            # res = [x for x in string if x == st[i] or x == st[j]]
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