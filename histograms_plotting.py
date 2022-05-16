# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:01:19 2022

@author: Иван
"""

import numpy,matplotlib.pyplot

randArray=numpy.random.rand(10000)+numpy.random.rand(10000)
gaussDraw=numpy.random.randn(100000)

matplotlib.pyplot.clf()
#matplotlib.pyplot.hist(randArray,bins=30)
matplotlib.pyplot.hist(gaussDraw,bins=40)

#saving the plot to a file
matplotlib.pyplot.savefig('figureName.pdf',bbox_inches='tight') #additional possible argument for pixel-based formats is dpi=300