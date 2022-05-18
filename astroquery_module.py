# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:33:42 2022

@author: Иван
"""

from astroquery.gaia import Gaia
import matplotlib.pyplot as plt

job=Gaia.launch_job("""
SELECT TOP 1000000
l,b
FROM gaiadr2.gaia_source
ORDER BY RANDOM_INDEX
""")
resultset=job.get_results()

plt.clf()
plt.hist2d((resultset['l']+180.0) % 360,resultset['b'], bins=(200,200), cmap=plt.cm.jet)
plt.savefig('gaia-plot2.pdf',bbox_inches='tight')