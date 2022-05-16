# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:25:44 2022

@author: Иван
"""

import numpy as np
Teff = 5780
R = 695500*1000
sigma=5.670367e-8

L = 4*np.pi*R**2*sigma*Teff**4
print(L)
