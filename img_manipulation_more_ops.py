# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:05:15 2022

@author: Иван
"""

from astropy.io import fits
import numpy
import matplotlib.pyplot as plt

hdulistS=fits.open('frame-g-007923-5-0307.fits')
imdataS=hdulistS[0].data

lowerOne=numpy.percentile(imdataS,1)
upperOne=numpy.percentile(imdataS,99)

plt.clf()
plt.imshow(imdataS,cmap='gray',clim=(lowerOne,upperOne))
#plt.savefig('sdss-py.pdf',bbox_inches='tight')
#%%
centerX=1819
centerY=1215
plt.imshow(imdataS,cmap='gray',clim=(lowerOne,upperOne))
plt.xlim(centerX-100,centerX+100)
plt.ylim(centerY-75,centerY+75)

thisCircle=plt.Circle((centerX,centerY),10,color='r',fill=False,lw=2)
plt.gca().add_artist(thisCircle)
thisCircle=plt.Circle((centerX,centerY),20,color='r',fill=False,lw=2)
plt.gca().add_artist(thisCircle)

