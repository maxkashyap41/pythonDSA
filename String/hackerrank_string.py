# input       : hereiamstackerrank
#               hackerworld
# output      : YES
#               NO
# explanation : The characters of hackerrank are bolded in the string above.
#               Because the string contains all the characters in hackerrank 
#               in the same exact order as they appear in hackerrank, we print YES on a new line.



def hackerRank(string):
    hacker = "hackerrank"
    flag = -1
    j = 0
    for i in range(len(string)):
        if string[i] == hacker[j]:
            j = j+1
        if j == len(hacker):
            flag = 1
            break
    
    print(j)
    if flag == 1:
        print("YES")
    else:
        print("NO")
    


if __name__ == "__main__":
    print("\n")
    string = "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
    hackerRank(string)
    print("\n")
