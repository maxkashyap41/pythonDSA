def Remain(string, char, counter):
    x = ''
    i = 0
    c = 0
    while i < len(string):
        if string[i] == char:
            if i < len(string)-1:
                c = c+1
                if c == counter:
                    x = x+string[i+1:len(string)]
                    return x
            else:
                x = x+'Empty string'
                return x

        i = i+1
    
    if counter == 0:
        return string
    elif char not in string:
        x = x+'Empty string'
        return x  
    elif c < counter:
        x = x+'Empty string'
        return x
    


if __name__ == "__main__":
    print("\n")

    # string = 'Thisisdemostring'
    # char = 'i'
    # counter = 3
    # string = 'Wearegeeks'
    # char = 's'
    # counter = 1
    string = 'Iamageek'
    char = 't'
    counter = 0
    # string = 'Helloeveryone'
    # char = 'y'
    # counter = 2
    # string = 'irrmxiyznkiooozxpiengefoeaxnzofjfxwffwgshojxekutsajygookpmy'
    # char = 'q'
    # counter = 11

    ans = Remain(string, char, counter)
    print(ans)

    print("\n")
