def search_engine(string):
    i = 0
    x = ""
    while i < len(string):
        x = x+string[i]
        if string[i-1] == "\\" and string[i] == "b":
            length = len(x)
            x = x[0:length-3]
        
        if string[i-1] == "\\" and string[i] == "n":
            x = x+"\n"
        i = i+1
    print(x)


if __name__ == "__main__":
    # string = str(input("\nEnter the String: "))
    print("\n")
    string = "This is a sample tests\b \nThis is a  \bnew line \nThis is also new line"
    search_engine(string)
    print("\n")