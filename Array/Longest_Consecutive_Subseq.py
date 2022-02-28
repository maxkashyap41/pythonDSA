def LongestConsec_Subseq(arr):
    s_arr = list(set(arr))
    s_arr.sort()    # since some compilers randomize the set so sorting will make efficient with all TCs
    n = len(s_arr)

    c_arr = []
    i = 0
    while i < n:
        c = 0
        while i != n-1 and s_arr[i] == s_arr[i+1]-1:
            c += 1
            i += 1
        c_arr.append(c+1)
        i += 1
    
    
    print(c_arr)
    print(max(c_arr))


if __name__ == "__main__":
    print("\n")

    arr = [36,41,56,35,44,33,34,92,43,32,42]
    # arr = [1,9,3,10,4,20,2]
    # arr = [36,41,44,35,45,33,34]
    # arr = [6,6,2,3,1,4,1,5,6,2,8,7,4,2,1,3,4,5,9,6]
    # arr = [8,9,1,2,3,1]
    LongestConsec_Subseq(arr)

    print("\n")
