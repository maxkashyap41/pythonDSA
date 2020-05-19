def LeetCode(arr, n, target):
    hashmap = {}
    result = []
    
    for i, num in enumerate(arr):
        ans = t-num
        if ans in hashmap:
            result.append(hashmap[ans])
            result.append(i)
            return result
        
        hashmap[num] = i



if __name__ == "__main__":
    print("\n")
    # arr = [2,7,11,34,5]
    # t = 9
    arr = [3,2,4]
    t = 6
    n = len(arr)

    res = LeetCode(arr, n, t)
    print("The List of Indexes are: ", res)
    
    print("\n")