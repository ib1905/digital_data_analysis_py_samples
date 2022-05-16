# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:02:51 2022

@author: Иван
"""

import numpy as np
from astropy import constants as const
from astropy import units as u

Teff=5780*u.K
R=const.R_sun

L=4*np.pi*R**2*const.sigma_sb*Teff**4
print(L)

#converting units
print((R.to(u.km)))
