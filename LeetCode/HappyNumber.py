# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


def LeetCode(num):
    if num < 10:
        num = num**2

    while num >= 10:
        sumRoot = 0
        while num > 0:
            rem = num % 10
            sumRoot = sumRoot+(rem**2)
            num = num // 10
    
        # print(sumRoot)
        num = sumRoot
        continue

    print(num)
    if num == 1 or num == 7:
        return True
    else:
        return False


if __name__ == "__main__":
    print("\n")
    # num = 19
    # num = 17
    # num = 7
    # num = 2
    num = 1111111

    if LeetCode(num) == True:
        print("True, it is Happy Number.")
    else:
        print("False, it is not a Happy Number.")
    print("\n")