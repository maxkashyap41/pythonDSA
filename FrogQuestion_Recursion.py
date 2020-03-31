def jumpSteps(rocks):
    if rocks == 1:
        return 1
    if rocks == 2:
        return 2
    
    return jumpSteps(rocks-1) + jumpSteps(rocks-2)


if __name__ == "__main__":
    rocks = int(input("\nEnter the Number of Rocks at the River: "))
    
    ways = jumpSteps(rocks)
    startToend = ways+1
    print("The Number of ways the Frog can jump from START to END ~ ", startToend)
    print("\n")