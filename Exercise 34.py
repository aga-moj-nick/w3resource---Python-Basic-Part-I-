# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

def sumowanie (a, b):
    if (a + b) in range (15, 21):
        return (20)
    else:
        return (a + b)

a = int (input ("Podaj liczbę a: "))
b = int (input ("Podaj liczbę b: "))
print ("Wynik dodawania to: ", sumowanie (a, b))
