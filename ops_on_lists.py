# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:27:54 2022

@author: Иван
"""

import numpy

galaxy_magnitude=[23.4, 23.2, 26.8, 24.6, 24.5, 24.3, 23.1, 27.0, 24.0]
print(galaxy_magnitude,'total number is',len(galaxy_magnitude))
'''
galaxy_flux=[]

#straightforward way
for magnitude in galaxy_magnitude:
    flux=3631*numpy.power(10,magnitude/(-2.5))
    galaxy_flux.append(flux)

print(galaxy_flux)

#function-type way
def flux(magnitude):
    return 3631*numpy.power(10,magnitude/(-2.5))

galaxy_flux=*map(flux,galaxy_magnitude), #note * and ,
print(galaxy_flux)
'''
#a list comprehension
galaxy_flux=[3631*numpy.power(10,magnitude/(-2.5)) for magnitude in galaxy_magnitude if magnitude<25]
print(galaxy_flux,'total number is',len(galaxy_flux))