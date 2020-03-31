if __name__ == "__main__":
    num = int(input("\nEnter the Number: "))
    for i in range(num, 0, -1):
        for j in range(0, num-i):
            print(end = " ")
        for j in range(0, i):
            print("*", end = " ")
        print("\n")
    
    print("\n")