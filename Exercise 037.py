# 37. Write a Python program to display your details like name, age, address in three different lines.


# ROZWIĄZANIE 1:
def dane_personalne ():

    imie = input ("Podaj swoje imię: ")
    nazwisko = input ("Podaj swoje nazwisko: ")
    wiek = input ("Podaj swój wiek: ")
    print ("imie: {} \nnazwisko: {} \nwiek: {}".format (imie, nazwisko, wiek))

dane_personalne ()


# ROZWIĄZANIE 2:
imie = input("Podaj swoje imię: ")
nazwisko = input ("Podaj swoje nazwisko: ")
wiek = input ("Podaj swój wiek: ")

print(f"Twoje imię to: {imie}")
print(f"Twoje nazwisko to: {nazwisko}")
print(f"Twój wiek to: {wiek}")

