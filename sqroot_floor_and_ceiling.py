import math


num = 0
sq = math.sqrt(num)

print(sq, math.floor(sq))
if sq - math.floor(sq) == 0:
    print("Yes")
else:
    print("No")