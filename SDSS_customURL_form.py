# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:19:30 2022

@author: Иван
"""

from subprocess import call

saveFileName = 'spectrum.fits'

run2d = 26
plate = 1324
mjd = 53088
fiberID = 456
baseURL = 'http://data.sdss3.org/sas/dr8/sdss/'
dirURL = f'spectro/redux/{run2d:d}/spectra/{plate:d}/'
fileURL = f'spec-{plate:d}-{mjd:d}-{fiberID:04d}'
url = baseURL+dirURL+fileURL+'.fits'
print(url)

#for Linux and Mac machines only
call(["curl", "-o", saveFileName, url])
