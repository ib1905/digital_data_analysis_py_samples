import pyvo
import matplotlib.pyplot as plt

serviceURL='https://gea.esac.esa.int/tap-server/tap'
service=pyvo.dal.TAPService(serviceURL)
resultset=service.search(
"""
SELECT TOP 1000000
l,b
FROM gaiadr2.gaia_source
ORDER BY RANDOM_INDEX
""")

plt.clf()
plt.hist2d((resultset['l']+180.0) % 360,resultset['b'], bins=(200,200), cmap=plt.cm.jet)
plt.savefig('gaia-plot.pdf',bbox_inches='tight')
