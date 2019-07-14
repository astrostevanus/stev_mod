import numpy as np
import h5py
import os

molid=np.array(['46Ti-16O__Toto', '47Ti-16O__Toto','48Ti-16O__Toto', '50Ti-16O__Toto'])

tpfilename='wasp33b-emi-haynes.prof'
tpfile=h5py.File(tpfilename,'r')
tcent=tpfile['T_layer (K)'][:]
pcent=tpfile['P_layer (bar)'][:]*0.986923

i=0

for tp in range(len(tcent)):
	os.system('./heliosk -name '+str(tpfilename)+'_'+str(molid[i])+'_layer_'+str(tp+1)+' -T '+str(tcent[i])+' -P '+str(pcent[i])+' -M '+str(molid[i])+' -numin 11000 -numax 17000 -path ./data/exomol/ -cut 1e30 -dnu 0.01')


