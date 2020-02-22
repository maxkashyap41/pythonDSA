# input        : dccdabaeffffgghhhi
#                k = 3
#
# output       : a
# 
# explanations : arrange the string according to frequency and from that return the kth largest character from the string
#                but if k -> 3 then
#                ['f', 'h', 'a', 'c', 'd', 'g', 'b', 'e', 'i']
#                [4, 3, 2, 2, 2, 2, 1, 1, 1]
#                then the character having frequency 2 (as it the 3rd largest in the frequency list) we shall determine 
#                the which is the smallest from them and print the character same as the vice versa 
#                for characters with frequency having 1 if k -> 4


def k_largest(string, k):
    stringList = []
    for i in range(len(string)):
        stringList.append(string[i])
    
    # print(stringList)
    
    list1 = []
    list2 = []
    visited = [False for _ in range(len(stringList))]

    for i in range(len(stringList)):
        if visited[i] == True:
            continue

        count = 1
        for j in range(i+1, len(stringList)):
            if stringList[i] == stringList[j]:
                visited[j] = True
                count = count+1
        
        # print(stringList[i], ":", count)
        
        list1.append(stringList[i]) # alpha values
        list2.append(count)         # counts


    for i in range(len(list1)-1):
        for j in range(len(list1)-i-1):
            if list2[j+1] > list2[j]:
                # counts
                temp = list2[j+1]
                list2[j+1] = list2[j]
                list2[j] = temp
                # alpha values
                temp = list1[j+1]
                list1[j+1] = list1[j]
                list1[j] = temp
            elif list2[j] == list2[j+1]:
                if list1[j] > list1[j+1]:
                    temp = list1[j]
                    list1[j] = list1[j+1]
                    list1[j+1] = temp
    
    print(list1)
    print(list2) 

    lastdigit = -999999
    count = 0
    for i in range(len(list2)):
        if list2[i] != lastdigit:
            lastdigit=list2[i]
            count = count+1
            # print(count)
        if count == k:
            print(list1[i])
            return
    print("-1")



if __name__ == "__main__":
    string = str(input("\nEnter the String: "))
    k = int(input("Enter the K: "))

    print("\nThe kth largest character: ")
    k_largest(string, k)
    print("\n")