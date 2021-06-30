# 44. Write a Python program to locate Python site-packages


import site
print("1: ", site.getsitepackages())


import sysconfig
print("2: ",sysconfig.get_paths()["purelib"])


import setuptools as _
print("3: ", _.__path__)


import os as _
print("4: ", _.__file__)


from distutils.sysconfig import get_python_lib
print("5: ", get_python_lib())


import distutils.sysconfig
print ("6: ", distutils.sysconfig.get_python_lib())
