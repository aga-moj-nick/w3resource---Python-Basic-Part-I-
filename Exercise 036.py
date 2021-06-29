# 36. Write a Python program to add two objects if both objects are an integer type.

def sumowanie (a, b):
    if not (isinstance (a, int)) or (isinstance (b, int)):
        return (False)
    else:
        return (a + b)

a = float (input ("Podaj a: "))
b = float (input ("Podaj b: "))
print ("Wynik to: ", sumowanie (a, b))
