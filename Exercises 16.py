# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

a = int (input ("Podaj liczbę a: "))
odejmowanie = int (a - 17)

if a >= 17:
    print(2 * (a - 17))
elif a < 17:
    print(abs(a - 17))




