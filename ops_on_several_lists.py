# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:15:35 2022

@author: Иван
"""

import numpy

#star apparent magnitudes in V band
st_appV=[-1.46, 5.2, 3.49, 0.76]

#distance from star in parsec
st_distPc=[2.64, 3.5, 3.65, 5.12]

print(st_appV,st_distPc)

#formula to calculate absolute magnitude M using apparent magnitude m and distance d
#M=m-5*log10*(d/10pc)

'''
#straighforward way
#star absolute magnitude
st_absV=[]
for star in range(len(st_appV)):
    thisM=st_appV[star]-5*numpy.log10(st_distPc[star]/10)
    st_absV.append(thisM)
print(st_absV)
'''
#lists comprehension
#star absolute magnitude
st_absV=[ magnitude-5*numpy.log10(distance/10) for magnitude,distance in zip(st_appV,st_distPc) ]
print(st_absV)

#to perfom 'zip' in console use *zip(list1,list2),
#example of output is a tuple: Out[8]: ((-1.46, 2.64), (5.2, 3.5), (3.49, 3.65), (0.76, 5.12))
#tuples are immutable unlike lists