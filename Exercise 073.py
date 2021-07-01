# 73. Write a Python program to calculate midpoints of a line. 


def punkt_środkowy (a1, a2, b1, b2):
    return ((a1 + a2) / 2, (b1 + b2) / 2)


a1 = float (input ("Podaj a1: "))
b1 = float (input ("Podaj b1: "))

a2 = float (input ("Podaj a2: "))
b2 = float (input ("Podaj b2: "))
print ("Punkt środkowy wynosi: ", punkt_środkowy (a1, a2, b1, b2))
