def Swap_Array(arr, a, brr, b):
    SumA = 0
    for i in range(a):
        SumA = SumA+arr[i]
    
    SumB = 0
    for i in range(b):
        SumB = SumB+brr[i]
    
    if SumA < SumB:
        z = SumB-SumA
    else:
        z = SumA-SumB
    
    if z % 2 == 0:
        z = z // 2
        if SumA < SumB:
            bth = z+1
            ath = z-(z-1)
            for i in range(a):
                if arr[i] == ath:
                    arr.remove(arr[i])
                    arr.append(bth)
                    break
            for i in range(b):
                if brr[i] == bth:
                    brr.remove(brr[i])
                    brr.append(ath)
                    break
            
            print(arr, brr)
            if sum(arr) == sum(brr):
                return 1
            else:
                return -1
        else:
            bth = z-(z-1)
            ath = z+1
            for i in range(a):
                if arr[i] == ath:
                    arr.remove(arr[i])
                    arr.append(bth)
                    break
            for i in range(b):
                if brr[i] == bth:
                    brr.remove(brr[i])
                    brr.append(ath)
                    break
            
            print(arr, brr)
            if sum(arr) == sum(brr):
                return 1
            else:
                return -1
    else:
        return -1


if __name__ == "__main__":
    print("\n")

    # arr = [4,1,2,1,1,2]
    # brr = [3,6,3,3]
    # arr = [5,7,4,6]
    # brr = [1,2,3,8]
    
    a, b = map(int, input("\nEnter the Size of the Arrays: ").split())
    arr = list(map(int, input("Array Elements: ").split()))[:a]
    brr = list(map(int, input("Brray Elements: ").split()))[:b]

    ans = Swap_Array(arr, a, brr, b)
    print("\nBoth the Array has pair or not ", ans)

    print("\n")
