# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:42:26 2022

@author: Иван
"""

import numpy

k=0.5
m=1.0
numberOfSteps=30000
DeltaT=0.001
finalT=numberOfSteps*DeltaT

#used only for plotting positions preparation
toCollector=numpy.linspace(0,finalT,numberOfSteps+1)

#initial conditions
xCollector=[1.0]
vCollector=[0]

for ii in range(numberOfSteps):
    xNew=xCollector[-1]+DeltaT*vCollector[-1]
    vNew=vCollector[-1]+DeltaT*(-k/m*xCollector[-1])
    xCollector.append(xNew)
    vCollector.append(vNew)