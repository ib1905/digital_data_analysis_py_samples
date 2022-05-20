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
#%%
#defining the sum of pixel brightness in the outer circle
radiusOut=20
photCollector=numpy.array([])
for ii in range(centerX-radiusOut,centerX+radiusOut):
    for jj in range(centerY-radiusOut,centerY+radiusOut):
        distance=numpy.sqrt((ii-centerX)**2+(jj-centerY)**2)
        if distance < radiusOut:
            photCollector=numpy.append(photCollector,imdataS[jj][ii])
C1=numpy.sum(photCollector)
A1=len(photCollector)

#and now the inner circle
radiusIn=10
photCollector=numpy.array([])
for ii in range(centerX-radiusIn,centerX+radiusIn):
    for jj in range(centerY-radiusIn,centerY+radiusIn):
        distance=numpy.sqrt((ii-centerX)**2+(jj-centerY)**2)
        if distance < radiusIn:
            photCollector=numpy.append(photCollector,imdataS[jj][ii])
C2=numpy.sum(photCollector)
A2=len(photCollector)

print('Outer radius','brightness:',C1,'area:',A1)
print('Inner radius','brightness:',C2,'area:',A2)

l=C2-((C1-C2)/(A1-A2)*A2) #brightness formula
print('{:.2f}'.format(l))

