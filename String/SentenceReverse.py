def sentenceReverse(string):
    length = len(string)
    x = ""
    origin = []
    last = []
    i = 0
    while i < length:
        x = x+string[i]
        xlen = len(x)
        if string[i] == " ":
            x = x[0:xlen-1]
            origin.append(x)
            x = ""
        i = i+1
    
    if i == length:
        xlen = len(x)
        x = x[0:xlen]
        last.append(x)

    # print(origin)
    # print(last)

    string1 = ''.join(last)

    origin.reverse()

    string2 = ' '.join(origin)
    
    result_string = string1+" "+string2
    print(result_string)



if __name__ == "__main__":
    string = str(input("\nEnter the String: "))
    print("After sentence Reversed: ", end = " ")
    sentenceReverse(string)
    print("\n")


