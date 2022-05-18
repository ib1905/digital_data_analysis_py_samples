# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:48:29 2022

@author: Иван
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy

fitsURL='hst_05773_05_wfpc2_f502n_wf_drz.fits'
hdulist=fits.open(fitsURL)

print(hdulist.info(),'\n')
print(hdulist[1].header,'\n')
print(hdulist[1].header['NAXIS1'],'\n')
print(hdulist[0].header['EXPTIME'],'\n')

#image data
imdata=hdulist[1].data

plt.clf()
plt.axes().set_aspect('equal')
plt.imshow(imdata,cmap='gray',clim=(numpy.percentile(imdata,1),numpy.percentile(imdata,99)))

#to retrieve a brightness value of some pixel
print(imdata[1400][1200])
#NB! Mind the coordinates order: imdata[y][x]