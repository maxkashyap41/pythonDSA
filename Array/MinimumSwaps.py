# Graph Algorithm 

import operator as op

def MinimumSwaps(arr, n):
    count = 0
    hasht = [*(enumerate(arr))]
    hasht.sort(key = op.itemgetter(1))

    checked = [False for k in range(n)]

    for i in range(n):
        if checked[i] == True:
            continue

        j = i
        c = 0
        while checked[j] == False:
            checked[j] = True
            j = hasht[j][0]
            c = c+1
        count = count + (c-1)
    
    return count
    


if __name__ == "__main__":
    print("\n")

    # arr = [4,3,2,1]
    # arr = [1,5,4,2,3]
    arr = [101,758,315,730,472,619,460,479]
    # arr = [1,2,3,4]
    n = len(arr)

    res = MinimumSwaps(arr, n)
    print(res)

    print("\n")