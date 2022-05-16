# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:15:53 2022

@author: Иван
"""

#catalogue numbers
nm=['SDSS-II SN 21387','SDSS-II SN 13651','SDSS-II SN 03706','SDSS-II SN 10963','SDSS-II SN 03475']
#distances in parsec
dpc=[4200.,1700.,3720.,577.,1040.]
#redshifts
zv=[0.48,0.25,0.44,0.09,0.3]
'''
#lengthy option
nmN=[]
dpcN=[]
zvN=[]

for i in range(len(nm)):
    if zv[i]>0.26:
        nmN.append(nm[i])
        dpcN.append(dpc[i])
        zvN.append(zv[i])
print(nmN,dpcN,zvN)
'''
#elegant option via list comprehension
nmN,dpcN,zvN=map(list, zip(*[(n,d,z) for n,d,z in zip(nm,dpc,zv) if z>0.26]))
#*zip inverts zipping
#here map function is used to apply list function to every tuple to turn it into list
print(nmN,dpcN,zvN)