# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:36:27 2022

@author: Иван
"""
string1 = 'ABC'
string2 = 'def'
concat_string = string1 + string2
stringAsList = 'ABCDEFGHIJKLMNOP'

print(concat_string)
print('G'+'H'+'I')

sampleNo = 10
sampleFl = 1.23456789012345
sampleBig = 123456789012345.678
sampleSmFl = 0.0001515
print('sampleName: {}'.format(sampleNo))
print('sampleNameDiff: {:04d}'.format(sampleNo))
print('sampleNameFl: {:f}'.format(sampleFl))
print('sampleNameFlDiff: {:.8f}'.format(sampleFl))
print('sampleNameBig: {:e}'.format(sampleBig))
print('sampleNameSm: {:e}'.format(sampleSmFl))
#below is a quite useful string formatting
print(f'sampleNameSm_new: {sampleSmFl:e}')
print('partOf_stringAsList_var:', stringAsList[3:6])
