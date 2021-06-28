# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

value = input ("Podaj trzy cyfry lub liczby oddzielone przecinkami: ")

list = value.split (',')
print ("List: ", list)

tuple = tuple (list)
print ("Tuple: ", tuple)
