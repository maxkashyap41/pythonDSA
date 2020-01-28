import math

def area(r):
    return math.pi * r ** 2

if __name__ == "__main__":
    radii_1 = [2, 5, 10, 23, 333, 12]
    radii_2 = [10, 5, 2, 7, 89, 35]

    areas = []

    for i in radii_1:
        a = area(i)
        areas.append(a)
    
    print("\n", areas)

    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    c = list(map(area, radii_2))
    print("\n", c)
