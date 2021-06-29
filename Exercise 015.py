# 15. Write a Python program to get the volume of a sphere with radius 6.

import math

# Dowolny promień:

def objetosc_kuli (r):
    return (4 / 3 * math.pi * r ** 3)

r = int (input ("Podaj r: "))
print ("Objętość kuli to: ", (4 / 3 * math.pi * r ** 3))


# Promień 6:
r = 6
objetosc_kuli = (4 / 3 * math.pi * r ** 3)

print ("Objętość kuli o promieniu 6 to: ", objetosc_kuli)
