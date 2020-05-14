# Removing k digits with continuos incrementing k


def LeetCode(string, k):
    result = []
    i = 0
    while i < len(string):
        x = ""
        j = i
        c = 1
        while c < k:
            j = j+1
            c = c+1
        
        if j == len(string):
            break
        
        x = x+string[0:i]+string[j+1:len(string)]
        print(x)
        
        result.append(x)
        i = i+1
    
    print(result)

    if all(i == '' for i in result):
        return "0"
    
    if any(int(i)+0 == 0 for i in result):
        return "0"
    else:
        ans = min(result)
        return ans.lstrip("0")
    


if __name__ == "__main__":
    print("\n")
    # string = "1432219"
    # k = 3
    # string = "10200"
    # k = 1
    # string = "10"
    # k = 2
    string = "10"
    k = 1
    # string = "100"
    # k = 1

    res = LeetCode(string, k)
    print("Answer is: ", res)

    print("\n")