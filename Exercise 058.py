# 58. Write a Python program to sum of the first n positive integers. 


lista = [-2, -1, 0, 0.5, 1, 1.5, 2]
lista2 = []

for element in lista:
    if element > 0:
        lista2.append (element)
        print (lista2)
       
        
for element in lista2:
    if element != int:
        lista2.remove (element)
        print (sum(lista2))
     
        
