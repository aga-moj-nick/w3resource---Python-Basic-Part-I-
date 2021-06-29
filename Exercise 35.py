# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

def wynik (a, b):
    if a == b:
        return (True)
    if a - b == 5 or b - a == 5:
        return (True)
    if a + b == 5:
        return (True)
    

a = int (input ("Podaj a: "))
b = int (input ("Podaj b: "))
print ("Wynik to: ", wynik (a, b))
