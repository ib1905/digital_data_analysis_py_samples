# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:53:20 2022

@author: Иван
"""

import time

start_time=time.time()
for ii in range(100000000):
    pass
end_time=time.time()

print('This took {:.2f} seconds'.format(end_time-start_time))