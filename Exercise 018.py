# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

n1 = int (input ("Podaj n1: "))
n2 = int (input ("Podaj n2: "))
n3 = int (input ("Podaj n3: "))

if n1 == n2 == n3:
    print ((n1 + n2 + n3) * 3)
else:
    print (n1 + n2 + n3)
