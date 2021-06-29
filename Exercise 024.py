# 24. Write a Python program to test whether a passed letter is a vowel or not.

samogłoski = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
głoska = input("Podaj głoskę do sprawdzenia: ")

def sprawdzanie (głoska):
    if głoska in samogłoski:
        print ("Podana głoska jest samogłoską")
    else:
        print ("Podana głoska nie jest samogłoską")
            
sprawdzanie (głoska)

