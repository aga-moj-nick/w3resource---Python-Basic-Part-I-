# 99. Write a Python program to clear the screen or terminal.


import os
from time import sleep

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
   
print("The platform is: ", os.name)
print("big output\n"* 5)

sleep(5)

screen_clear()
