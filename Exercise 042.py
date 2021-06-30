# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.


import ctypes
print (ctypes.sizeof(ctypes.c_voidp))


import struct
print (struct.calcsize("P") * 8)


import platform
print(platform.architecture())



