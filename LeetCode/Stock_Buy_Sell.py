# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

def LeetCode(arr, n):
    count = 0
    i = 0
    while i < n:
        if i < n-1 and arr[i] < arr[i+1]:
            buy = arr[i]
            # print(buy)
            j = i+1
            while j < n-1 and arr[j] < arr[j+1]:
                j = j+1
            sell = arr[j]
            # print(sell)
            count = count+(sell-buy)
            i = j+1
        else:
            i = i+1
    
    return count


if __name__ == "__main__":
    print("\n")
    # arr = [1,2,3,4,0]
    # arr = [7,1,5,3,6,4]
    # arr = [1,2,3,4,5]
    arr = [7,6,4,3,1]
    n = len(arr)
    print(arr)
    res = LeetCode(arr, n)
    print(res)
    print("\n")
