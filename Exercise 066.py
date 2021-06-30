# 66. Write a Python program to calculate body mass index

def BMI (masa, wzrost):
    return masa / wzrost ** 2

masa = float (input ("Ile kg? "))
wzrost = float (input ("Ile m? " ))
print ("BMI to: ", BMI (masa, wzrost))


