# 38. Write a Python program to solve (x + y) * (x + y).

def liczenie (a, b):
    return ((a + b) ** 2)

a = float (input ("Podaj liczbę a: "))
b = float (input ("Podaj liczbę b: "))

print ("Wynik liczenie to: ", liczenie (a, b))

