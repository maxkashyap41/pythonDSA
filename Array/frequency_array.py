# frequency of array using dictionary

def missingNumbers(arr, n):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] = freq[i]+1
        else:
            freq[i] = 1
    
    for key, value in freq.items():
        print("%d : %d"% (key, value))


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7, 8, 3, 4, 5, 6]
    n = len(arr)
    print("\n")
    missingNumbers(arr, n)
    print("\n")