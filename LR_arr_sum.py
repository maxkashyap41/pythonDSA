# Sum of left array is equal to right array
# i/p:- 1 2 2 9 4 1,    o/p:- 5, 9

def left_right_sum(arr):
    left_array = 0
    right_array = 0
    i = 1
    j = 0
    for i in range(1, len(arr)):
        right_array = right_array + arr[i]

    for i in range(1, len(arr)):
        if j == len(arr):
            break
        right_array = right_array - arr[i]
        left_array = left_array + arr[j]

        if right_array == left_array:
            return left_array, arr[j+1]
        
        j = j + 1
        

if __name__ == "__main__":
    arr = [1, 2, 2, 9, 1, 4]
    result = left_right_sum(arr)
    print("\nThe Middle Element is : ", result)
