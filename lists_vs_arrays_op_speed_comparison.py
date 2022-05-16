# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:03:26 2022

@author: Иван
"""

import time
import numpy

numberlist=[ii for ii in range(100000000)]
numberarrIt=numpy.array(numberlist)
numberarr=numpy.array(numberlist)

start_time=time.time()
for ii in range(len(numberlist)):
    numberlist[ii]=2*numberlist[ii]
end_time=time.time()
print('Operation on list took {:.4g} seconds'.format(end_time-start_time))

start_time=time.time()
numberarr=numberarr*2
end_time=time.time()
print('Operation on array took {:.4g} seconds'.format(end_time-start_time))
