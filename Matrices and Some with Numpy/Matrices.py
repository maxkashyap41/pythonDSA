import numpy as np


if __name__ == "__main__":
    print("\n")

    arr = np.array([
        [1,2,3,4,5],
        [6,7,8,9,10]
    ])
    
    print(arr, "\n")
    print(arr.size, arr.ndim)
    print("\n")

    brr = arr.flatten()     # it bascially flattens the whole dimensions of array into 1D. 
    print(brr, "\n")

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

    crr = np.array([
        [2,3,4,5,7,9],
        [1,3,5,7,9,11]
    ])

    drr = crr.flatten()
    frr = drr.reshape(3,4)      # it reshapes the 1D array into 2D.
    grr = drr.reshape(2,2,3)    # it reshapes the 1D array inot two different 2Ds. np.reshape(no. of 2Ds, Rows, Cols)

    print(crr, "\n")
    print(drr, "\n")
    print(frr, "\n")
    print(grr, "\n")

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    print("----- | MATRIX | -----\n")

    m1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
    print(m1, "\n")
    print(" Diagonal values of the MATRIX !", np.diagonal(m1), "\n")

    m2 = np.matrix('3 4 5; 7 8 9; 10 12 14')
    m3 = m1+m2
    m4 = m1*m2
    print("\nAddition and Multiplication of 2 MATRCES !!!")
    print(m3, "\n")
    print(m4, "\n")

    print("\n")