import numpy as np

if __name__ == "__main__":
    print("\n")

    print("------- | ARRAY MULTIPLICATION | -------\n")
    arr = np.array([
        [2,4],
        [6,8]
    ])

    brr = np.array([
        [7,5],
        [3,1]
    ])

    crr = arr*brr
    print(crr, "\n")

    print("------- | MATRIX MULTIPLICATION | -------\n")
    m1 = np.matrix('2 4; 6 8')
    m2 = np.matrix('7 5; 3 1')
    
    print(m1, "\n")
    print(m2, "\n")

    ans = m1*m2
    print("Answer for Matrix: ")
    print(ans)

    print("\n")