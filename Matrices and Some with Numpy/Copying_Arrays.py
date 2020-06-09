import numpy as np

if __name__ == "__main__":
    print("\n")

    arr = np.array([2,4,6,8,10,12])
    brr = arr
    crr = arr.copy()                # known as the deep copy where another address of C_array has been created 
                                    # by copying the values of A_array

    arr[3] = 18
    arr[4] = 20

    print(arr, "\n")
    print(brr, "\n")
    print(crr, "\n")

    print(arr.ndim)
    print(id(arr))
    print(id(brr))
    print(id(crr))

    print("\n")