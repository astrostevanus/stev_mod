from PyAstronomy import pyasl
import numpy as np
import h5py
from tqdm import tqdm

xs=np.loadtxt('kurucz.list',unpack=True,dtype=str)

name=[]
for i in range(len(xs)):
	name.append(xs[i][18:-4])

h5f_harps=h5py.File('kelt20b-iso-2500K-trans-kurucz-nohmin.h5', 'r')

h5f_carm=h5py.File('kelt20b-iso-2500K-trans-kurucz-nohmin-carmenes.h5', 'w')

wvharsp=h5f_harps["wavelength"][:]
for i in tqdm(range(len(name))):
    spec=h5f_harps["spec_"+str(name[i])][:]
    rflx_hds = pyasl.instrBroadGaussFast(wvharsp, spec,94600,edgeHandling="firstlast")
	
    h5f_carm.create_dataset("spec_"+str(name[i]),data=rflx_hds, compression="gzip",compression_opts=9)

h5f_carm.create_dataset("wavelength",data=wvlair_hires, compression="gzip",compression_opts=9)

h5f_carm.close()
h5f_harps.close()
