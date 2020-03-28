def findOne(string):
    arr = []
    for i in range(len(string)):
        arr.append(string[i])
    
    print(arr)
    n = len(arr)

    for i in range(n-1, -1, -1):
        if arr[i] == '1':
            return i

    return -1

if __name__ == "__main__":
    print("\n")

    # string = "00001"
    # string = "0010111100"
    string = "00000"

    index = findOne(string)
    print("The Last Index of One is :~ ", index)

    print("\n")
