#  How do you calculate the distance between coordinates (x1,y1) and (x2,y2)?

import math



x1 = -6
y1 = -9
x2 = 5
y2 = 7

#calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(format(distance, ".1f"))