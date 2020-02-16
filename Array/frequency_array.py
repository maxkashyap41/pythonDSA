def frequency(arr, n):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] = freq[i]+1
        else:
            freq[i] = 1

    for key, value in freq.items():    
        print("%d : %d"% (key, value))

if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    print("Frequency of Array of Elements: ")
    frequency(arr, n)
    print("\n")