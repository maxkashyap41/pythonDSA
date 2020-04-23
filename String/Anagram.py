def Anagram(str1, str2):
    print(str1)
    print(str2)

    if sorted(str1) == sorted(str2):
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    str1, str2 = map(str, input("\nEnter the Strings: ").split())
    
    Anagram(str1, str2)

    print("\n")