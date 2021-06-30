# 59. Write a Python program to convert height (in feet and inches) to centimeters.

def cm (stopa, cal):
    return (2.54 * (12 * stopa + cal))

stopa = float (input ("Ile stóp? "))
cal = float (input ("Ile cali? "))
print ("Ile centymetrów?", cm (stopa, cal))
