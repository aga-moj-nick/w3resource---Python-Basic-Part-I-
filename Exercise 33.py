# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.


def sumowanie (a, b, c):
    if a == b == c:
        return (0 + 0 + 0)
    elif a == b:
        return (0 + 0 + c)
    elif b == c:
        return (a + 0 + 0)
    elif a == c:
        return (0+ b + 0)
    else:
        return (a + b + c)

a = int (input ("Podaj liczbę a: "))
b = int (input ("Podaj liczbę b: "))
c = int (input ("Podaj liczbę c: "))
print ("Wynik dodawania to: ", sumowanie (a, b, c))
        
