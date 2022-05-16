# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:03:03 2022

@author: Иван
"""

import matplotlib.pyplot as plt

#catalogue numbers
nm=['SDSS-II SN 21387','SDSS-II SN 13651','SDSS-II SN 03706','SDSS-II SN 10963','SDSS-II SN 03475']
#distances in parsec
dpc=[4200.,1700.,3720.,577.,1040.]
#redshifts
zv=[0.48,0.25,0.44,0.09,0.3]
#this data is chosen arbitrarily for the sa
sizes=[40,15,25,80,38]

plt.clf() #cleans the screen
#a Hubble diagram as a 'scatter' function representation of data points as separate markers with some minor customization
plt.scatter(zv,dpc,s=sizes,color='r') #we can add marker='^'
'''
alternative way to plot a scatter
plt.plot(zv,dpc,'o')
'''