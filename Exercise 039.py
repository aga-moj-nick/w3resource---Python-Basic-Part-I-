# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.


# Wzór1
def przyszla_wartosc (kwota_glowna, stopa_procentowa, lata):
    return ((kwota_glowna * stopa_procentowa * lata)/100)

kwota_glowna = float (input ("Podaj kwotę główną: "))
stopa_procentowa = float (input ("Podaj stopę procentową: "))
lata = int (input ("Podaj liczbę lat: "))
print ("Przyszła wartość wynosi: ", przyszla_wartosc (kwota_glowna, stopa_procentowa, lata))


# Wzór2
def przyszla_wartosc (kwota_glowna, stopa_procentowa, lata):
    return ((kwota_glowna * (1 + stopa_procentowa) ** lata))

kwota_glowna = float (input ("Podaj kwotę główną: "))
stopa_procentowa = float (input ("Podaj stopę procentową: "))
lata = int (input ("Podaj liczbę lat: "))
print ("Przyszła wartość wynosi: ", przyszla_wartosc (kwota_glowna, stopa_procentowa, lata))


# Wzór3
def przyszla_wartosc (kwota_glowna, stopa_procentowa, lata):
    return (kwota_glowna * (1 + (0.01 * stopa_procentowa)) ** lata)

kwota_glowna = float (input ("Podaj kwotę główną: "))
stopa_procentowa = float (input ("Podaj stopę procentową: "))
lata = int (input ("Podaj liczbę lat: "))
print ("Przyszła wartość wynosi: ", przyszla_wartosc (kwota_glowna, stopa_procentowa, lata))
