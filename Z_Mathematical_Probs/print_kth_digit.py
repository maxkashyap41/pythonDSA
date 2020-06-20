# https://practice.geeksforgeeks.org/problems/print-the-kth-digit/0/

def Kth_digi(A, B, k):
    num = A ** B

    while k and num != 0:
        k_pos_ans = num % 10
        num = num // 10
        k = k-1
    
    return k_pos_ans


if __name__ == "__main__":
    # A = 3    A = 5 
    # B = 3    B = 2
    # k = 1    k = 2

    A, B, k = map(int, input("\nEnter the A B and also the k: "))
    ans = Kth_digi(A, B, k)
    print(ans)

    print("\n")