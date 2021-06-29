# 30. Write a Python program that will accept the base and height of a triangle and compute the area.


def powierzchnia_trojkata (a, H):
    return (a * H) / 2

bok = int (input("Podaj a: "))
wysokosc = int (input ("Podaj H: "))
                     
print ("Powierzchnia trójkąta to: ", powierzchnia_trojkata (bok, wysokosc))

