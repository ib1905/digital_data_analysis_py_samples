# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:27:49 2022

@author: Иван
"""

import numpy
import matplotlib.pyplot

x=numpy.linspace(0,2*numpy.pi,200)
y=numpy.sin(x)

matplotlib.pyplot.clf() #clears all previous plots
#matplotlib.pyplot.figure(figsize=(6,2))
matplotlib.pyplot.xlabel('Time in seconds')
matplotlib.pyplot.ylabel('Pendulum angle [arbitrary units]')
matplotlib.pyplot.axhline(0.0,color='g')
matplotlib.pyplot.axvline(0.5,color='m')
matplotlib.pyplot.annotate('intersection point',xy=(numpy.pi,0),xytext=(4,0.3),arrowprops={'arrowstyle':'-|>'})
matplotlib.pyplot.xlim(0,2*numpy.pi)
matplotlib.pyplot.ylim(-1.2,1.2)
matplotlib.pyplot.plot(x,y,'r',lw=3,linestyle='dashed')