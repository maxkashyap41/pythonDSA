import numpy as np

if __name__ == "__main__":
    print("\n")

    arr = np.array([2,6,7,12,67,900])
    brr = arr + 120
    crr = np.array([23, 78,45,122,90,78])
    drr = arr + crr
    err = np.cos(arr)
    frr = np.sin(arr)
    grr = np.tan(arr)
    hrr = np.concatenate([arr, crr])

    print(arr, "\n")
    print(brr, "\n")
    print(drr, "\n")
    print(err, "\n")
    print(frr, "\n")
    print(grr, "\n")
    print(hrr, "\n")

    print("\n")
