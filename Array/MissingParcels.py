# Amazon Code
# Given the parcelIds which are already added in the shipment
# find the minimum possible cost of shipping the items added to complete
# the load.

# Input: Arr = [2, 3, 6, 10, 11]
#        k = 9
# Output: 17
# Explanation: ParcelIds range from 1 through infinity. After reviewing
#              the current manifest, the remaining parcels to choose from
#              are [1,4,5,7,8,9,12,13....]. There are 5 parcels already on the truck
#              and it can carry k=9 parcels when fully loaded. Choose 4 more packages
#              to include [1,4,5,7] as their shipping cost is 1+4+5+7=17 which is minimal and return 17.
#
#
# Input: Arr = [6, 5, 4, 1, 3]
#        k = 7
# Output: 9
# Explanation: The shipment already has 5 parcels and needs 2 more.
#              The parcels [2,7] can be added to have the shipment of exactly
#              7 parcels, [1,2,3,4,5,6,7]. The additional cost is 2+7=9
#               


def missingParcels(arr, n, k):
    newArr = []

    if k == n:
        return 0
    
    arr.sort()
    maxParcelId = max(arr)
    naturalNumberSum = maxParcelId*(maxParcelId+1) // 2
    arrSum = sum(arr)
    missingNumberSum = naturalNumberSum - arrSum

    i = 1
    j = 0
    remainingParcels = k-n
    counter = 0
    while missingNumberSum != 0:
        if i == arr[j]:
            j += 1
        else:
            if counter == remainingParcels:
                break
            missingNumberSum -= i
            newArr.append(i)
            counter += 1
        i += 1
    
    
    while counter != remainingParcels:
        maxParcelId += 1
        newArr.append(maxParcelId)
        counter += 1

    print(newArr)
    return sum(newArr)



if __name__ == "__main__":
    print("\n")

    # arr = [4,5,7,1]
    # k = 4
    arr = [2,3,6,10,11]
    k = 9
    # arr = [6,5,4,1,3]
    # k = 7
    n = len(arr)
    
    minCost = missingParcels(arr, n, k)
    print(minCost)

    print("\n")