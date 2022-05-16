# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:21:17 2022

@author: Иван
"""

galaxy_u=[23.4, 23.2, 26.8, 24.6, 24.5, 24.3, 23.1, 27.0, 24.0]

#galaxy=int
print('Original list:')
for galaxy in galaxy_u:
    print(galaxy)
#print(galaxy_u[0],galaxy_u[1])
print('max:',max(galaxy_u))
print('min:',min(galaxy_u))
print('len:',len(galaxy_u))

#slicing
print(galaxy_u[1:3])
print(galaxy_u[:3])
print(galaxy_u[5:-1]) #up to the end excl. the last element

#changes to lists
print('Modified list:')
galaxy_u.append(25.1)
for galaxy in galaxy_u:
    print(galaxy)
#galaxy_u.pop() #removes the last element