# A module is a simple python file(.py)
# It contains code - Functions, Classes , Variables that you can use 

# Two types - 1) Inbuild  2)Manuly

"""
import random
import math
import string
"""
#Manulay Build Modules
import my_package.Souptik_module as Souptik_module

print(Souptik_module.add(10,10))
print(Souptik_module.sub(10,10))
print(Souptik_module.mul(10,10))
print(Souptik_module.div(10,10))

from my_package.Souptik_module import power
print(Souptik_module.power(10,2))

#Manulay Build Modules
from my_package import Souptik_module,Souptik_module2
from my_package.Souptik_module import power

print(Souptik_module2.to_upper("souptik"))
print(Souptik_module.power(10,2))