# input :       aaabccddd
# ouput :       abd
# explanation : aaabccd -> abccd -> abd


def removalPairElements(string):
    i = 1
    while i < len(string):
        if string[i-1] == string[i]:
            string = string[0:i-1] + string[i+1:]
            i = 1
        i = i+1
    
    if not string:
        print("\nEmpty !")
    else:
        print("\nReduced String: "+ string)


if __name__ == "__main__":
    string = str(input("\nEnter the String: "))

    removalPairElements(string)
    print("\n")