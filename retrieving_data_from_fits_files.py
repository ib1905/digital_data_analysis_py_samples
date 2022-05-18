# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.cl
"""

from astropy.io import fits

hdulist=fits.open('zoo2MainSpecz.fits')
#HDU: header/data units

#to read from a csv file
#from astropy.io import ascii
#tdata2=ascii.read('zoo2MainSpecz.csv')

print(hdulist.info()) #brief table of contents
print(hdulist[1].columns) #columns names and data types

tdata=hdulist[1].data #accessing data from the table
print(tdata)

#output specified table cell
print(tdata.field('specobjid')[2])