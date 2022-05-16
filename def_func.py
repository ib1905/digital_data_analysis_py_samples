# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:33:23 2022

@author: Иван
"""

#our polynomial function f(x)=2x^2-x
def polyFunc(x):
    return 2*x**2-x

#alternative defining of our function
polFunc = lambda x: 2*x**2-x

a=2
b=4
print(polyFunc(a))
print(polyFunc(b))

print(polFunc(a))
print(polFunc(b))
