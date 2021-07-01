# 83. Write a Python program to test whether all numbers of a list is greater than a certain number.


def większe_od (a):
    for i in a:
        if i > 10:
            return True
        else:
            return False

a = [11, 12, 20]
print (większe_od (a))
