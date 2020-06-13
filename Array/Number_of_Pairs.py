import bisect as bt

def Count(brr, m, x, hashY):
    if x == 0:
        return 0
    
    if x == 1:
        return 0
    
    idx = bt.bisect_right(brr, x)
    # print(idx)
    count = m-idx
    count = count + (hashY[0] + hashY[1])

    if x == 2:
        count = count - (hashY[3] + hashY[4])
    
    if x == 3:
        count = count+hashY[2]
    
    return count



def Number_Pairs(arr, brr, n, m):
    hashY = [0 for i in range(5)]

    for i in range(m):
        if brr[i] < 5:
            hashY[brr[i]] = hashY[brr[i]]+1
    
    brr.sort()
    total_count = 0
    for x in arr:
        total_count = total_count+Count(brr, m, x, hashY)
    
    return total_count


if __name__ == "__main__":
    print("\n")

    # arr = [3,7,9,4]
    # brr = [5,6,11,2]
    arr = [2,1,6]
    brr = [1,5]
    n = len(arr)
    m = len(brr)

    res = Number_Pairs(arr, brr, n, m)
    print("\nAnswer: ", res)

    print("\n")
