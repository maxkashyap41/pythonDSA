# input :       aaabccddd
# ouput :       abd
# explanation : aaabccd -> abccd -> abd



def reduced(string):
    i = 0
    while i < len(string):
        if string[i] == string[i-1]:
            string = string[0:i-1]+string[i+1:]
            i = 0
        i = i+1
    if not string:
        print("\nEmpty !")
    else:
        print("\nReduced String is: " + string)


if __name__ == "__main__":
    string = str(input("\nEnter the String Input: "))
    reduced(string)
    print("\n")