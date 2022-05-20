# -*- coding: utf-8 -*-

mSirius=-1.5 #magnitude of Sirius
mUnknown=8.5
mPolaris=2.0 #magnitude of Polaris

#magnitude equation
bS_bU_ratio=((100**0.2)**(mUnknown-mSirius))
bS_bP_ratio=((100**0.2)**(mPolaris-mSirius))

print('Brightness ratio between Sirius and Unknown: {:,.0f}'.format(bS_bU_ratio))
print('Sirius apparent brightness is {:,.0f} times greater than Polaris apparent brightness'.format(bS_bP_ratio))