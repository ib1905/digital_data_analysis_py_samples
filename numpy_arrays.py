# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:51:00 2022

@author: Иван
"""

import numpy

a=numpy.array([1.0,2.0,3.0,4.0])
print(a)

b=a*2
print(b)

c=b+1.5*a
print(c)

#dtype defines specific type of array element
floatArray=numpy.array([1,2,3,4], dtype='float32')
print(floatArray)