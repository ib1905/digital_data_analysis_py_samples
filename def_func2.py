# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:40:37 2022

@author: Иван
"""

import numpy as np

def zeroSqrt(x):
    if x<0:
        return 0
    else:
        return np.sqrt(x)

print(zeroSqrt(-1))
print(zeroSqrt(4))
print(zeroSqrt(0))
