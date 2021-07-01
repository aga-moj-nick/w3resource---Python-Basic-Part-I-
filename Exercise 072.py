# 72. Write a Python program to get the details of math module.


import math

math_module = dir(math)
print("Module math: ", math_module)


import stat

stat_module = dir (stat)
print ("Module stat: ", stat_module)


import datetime

datetime_module = dir (datetime)
print ("Module datetime: ", datetime_module)
