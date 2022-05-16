# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:39:51 2022

@author: Иван
"""

specObjID=1490816872793270272
bin_specObjID=bin(specObjID)[2:].zfill(64)
#using slicing here to get rid of '0b' which is to specify a following binary number in a from of a string
#zfill adds zeros to restore 64 bits instead of 61

#int base 2 converts binary back into integer
plate_specObjID=int(bin_specObjID[0:14],2)
fiber_specObjID=int(bin_specObjID[14:26],2)
MJD_specObjID=int(bin_specObjID[26:40],2)
rerun2d_specObjID=int(bin_specObjID[40:54],2)

print(specObjID,bin_specObjID)
print('plate: {}\nfiberID: {}\nMJD: {}\nrerun2d: {}'.format(plate_specObjID,fiber_specObjID,MJD_specObjID,rerun2d_specObjID))