# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

a1 = float (input ("Podaj a1: "))
b1 = float (input ("Podaj b1: "))
punkt1 = (a1, b1)


a2 = float (input ("Podaj a2: "))
b2 = float (input ("Podaj b2: "))
punkt2 = (a2, b2)

odległość = (((a2 - a1)** 2 + (b2 - b1)** 2)/2)

print (odległość)
