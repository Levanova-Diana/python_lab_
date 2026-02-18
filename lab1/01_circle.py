radius = 42
pi = 3.1415926
square = pi * radius * radius
print(round(square,4))

point_1 = (23, 34)
distance1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(distance1 <= radius)

point_2 = (30, 30)
distance2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
print(distance2 <= radius)

