# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

liczba = int (input ("Podaj liczbę: "))

if liczba in range (100, 1001) or liczba in range (100, 2001):
    print ("Jest")
else:
    print ("Nie ma")

"""
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))
"""
