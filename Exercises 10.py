# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 

n = int(input("Enter a number: "))
num = (n + ((n *10) + n) + ((n * 100) + (n * 10) + n))
print(num)
