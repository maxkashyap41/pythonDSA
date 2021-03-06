# Given an array of penalties P, an array of car numbers C, and also the date D.
# The task is to find the total fine which will be collected on the given date.
# Fine is collected from odd-numbered cars on even dates and vice versa.

def CollectFine(Crr, Frr, n, date):
    if date % 2 == 0:
        fine = 0
        for i in range(n):
            if Crr[i] % 2 != 0:
                fine = fine+Frr[i]
    else:
        fine = 0
        for i in range(n):
            if Crr[i] % 2 == 0:
                fine = fine+Frr[i]
    

    return fine


if __name__ == "__main__":
    print("\n")

    # date = 12
    # Crr = [2375, 7682, 2325, 2352]
    # Frr = [250, 500, 350, 200]
    # n = len(Crr)

    date = 8
    Crr = [2222,2223,2224]
    Frr = [200,300,400]
    n = len(Crr)

    fine = CollectFine(Crr, Frr, n, date)
    print(fine)

    print("\n")
