# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:14:53 2022

@author: Иван
"""

import numpy

k=5.0
m=1.0
numberOfSteps=30000
DeltaT=0.001
finalT=numberOfSteps*DeltaT

tCollector=numpy.linspace(0,finalT,numberOfSteps+1)

#initial conditions
xCollectorVV=[1.0]
vCollectorVV=[0]

for ii in range(numberOfSteps):
    vHalf=vCollectorVV[-1]+0.5*DeltaT*(-k/m*xCollectorVV[-1])
    xNew=xCollectorVV[-1]+DeltaT*vHalf
    vNew=vHalf+0.5*DeltaT*(-k/m*xNew)
    xCollectorVV.append(xNew)
    vCollectorVV.append(vNew)