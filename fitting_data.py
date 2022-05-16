# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:56:59 2022

@author: Иван
"""

import numpy
from scipy.optimize import curve_fit

def fitFunc(x,a):
    return x*a

#The Hubble-Lemaitre relation: z=H0/c*d, where H0 is the Hubble constant, c - the vacuum speed of light with redshift 'z' and distance 'd'.

#distances in parsec
dpc=[4200.,1700.,3720.,577.,1040.]
#redshifts
zv=[0.48,0.25,0.44,0.09,0.3]
'''
#polyfit function accepts zv as x values, dpc as y values with a polynomial of degree 1 with a linear function y=a*x+b; the function returns 'a' and 'b'
popt,pcov=numpy.polyfit(zv,dpc,1,cov=True)
perr=numpy.sqrt(numpy.diag(pcov))
print(popt,perr)
'''
#another fitting function with no offset: y=a*x
#popt finds best-fit values for free parameters
#perr extracts associated statistical errors
popt,pcov=curve_fit(fitFunc,zv,dpc)
perr=numpy.sqrt(numpy.diag(pcov))
print(popt,perr)