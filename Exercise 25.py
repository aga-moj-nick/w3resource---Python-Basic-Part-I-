# 25. Write a Python program to check whether a specified value is contained in a group of values.

wartości = [1, 2, 3, 4, 5]
wartości1 = [6, 7, 8, 9, 10]

wartość = int (input("Podaj swoją liczbę od 1 do 10: "))

def sprawdzanie (wartość):
    if wartość in wartości:
        print ("Podana liczba znajduje się na liście wartości")
    elif wartość in wartości1:
        print ("Podana liczba znajduje się na liście wartości1")
    else:
        print ("Nie ma takiej liczby na żadnej liście")
sprawdzanie (wartość)
