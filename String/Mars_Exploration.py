def mars_exploration(string):
    length = len(string)
    sos = "SOS"
    count = 0
    i = 0
    while i < length:
        if string[i] != sos[i%3]:
            count = count+1
        i = i+1
    
    return count


if __name__ == "__main__":
    string = "SOSSOSSOSSOS"
    res = mars_exploration(string)
    print("\n")
    print(res)
    print("\n")