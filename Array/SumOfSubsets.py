subsetArr = []

def subsetSum(arr, l, r, Sum=0):
    if l > r:
        subsetArr.append(Sum)
    else:
        subsetSum(arr, l+1, r, Sum+arr[l])
        subsetSum(arr, l+1, r, Sum)


if __name__ == "__main__":
    t = int(input("\nEnter the Testcases you wanna try: "))
    while t:
        n = int(input("\nEnter the Size of the Array: "))
        arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

        subsetSum(arr, 0, n-1)
        subsetArr.sort()
        for i in range(len(subsetArr)):
            print(subsetArr[i], end = " ")

        subsetArr.clear()
        print("\n")
        t = t-1