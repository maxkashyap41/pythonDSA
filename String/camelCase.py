# input       : saveChangeInTheEditor
# output      : 5
# explanation : count the number of words


def camelCase(string):
    length = len(string)
    
    i = 0
    count = 0
    while i < length:
        if string[i] == string[i].upper() or i == (length-1):
            count = count+1
        i = i+1
    
    print("\nCount is: ", count)


if __name__ == "__main__":
    string = str(input("\nEnter the String: "))
    camelCase(string)
    print("\n")