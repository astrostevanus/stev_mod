import warnings
warnings.filterwarnings('ignore')
from PyAstronomy import pyasl
import numpy as np
import h5py
from scipy import interpolate
import astropy.units as u
import astropy.constants as const
from tqdm import tqdm

def f_slow(lmbd):
    cn=[152.519,49.534,-118.858,92.536,-34.194,4.982]
    lmbd0=1.6419 #micron
    f=[]
    for i in range(len(cn)):
        f.append(cn[i]*(1./lmbd-1./lmbd0)**(i/2.))
    return np.sum(f,axis=0)
def xs_hmin(lmbda):
    #input is in Angstrom
    lmbd0=1.6419 #micron
    lmbd=lmbda*1e-4
    xs=1e-18*lmbd**3*(1./lmbd-1./lmbd0)*1.5*f_slow(lmbd)
    return xs

def rayscatt(wv):
    w=wv*1.e-8 #input is in angstrom, w is in cm
    alpha=0.8042*1e-24 #polarizability of molecular hydrogen
    acRAY=(128.*np.pi**5*(w)**-4*alpha**2)/3.
    return acRAY #cm2/molecule

def vac2air(wv_vac):
    s = 10.**4 /wv_vac
    n = 1.+0.0000834254+0.02406147/(130.-s**2)+0.00015998/(38.9-s**2)
    wv_air=wv_vac/n
    return wv_air

t= 2500
vmrhmin= 5e-10
planetname= 'kelt20b'
name1= 'Fe_I'
name2= 'Fe_II'

tpfilename=str(planetname)+'-'+str(t)+'K.prof'
tpfile=h5py.File(tpfilename,'r')
tcent=tpfile['T_layer (K)'][:]
pcent=tpfile['P_layer (bar)'][:]
tlist=tpfile['T_bound (K)'][:]
zlist=tpfile['z_bound (K)'][:]
zcent=(zlist[1:]+zlist[:-1])/2.
nlist=tpfile['n_density (element.cm-3)'][:]
Mp,Rp,Rs,mu,k,P0=tpfile['Mp_Rp_Rs_mu,k,P0'][:]
tpfile.close()

h5f_spec= h5py.File(str(planetname)+'-'+str(t)+'K-iso-trans-kurucz_'+str(name1)+'_'+str(name2)+'.h5', 'w')


h5f_cc=h5py.File('xs-'+str(t)+'K-kurucz.h5', 'r')

trspecall=[]
spec1=h5f_cc['spec_'+str(name1)][:]
wvl_1,xs_1=spec1[0],spec1[1]

spec2=h5f_cc['spec_'+str(name2)][:]
wvl_2,xs_2=spec2[0],spec2[1]

wvl_=wvl_1

n_density=(nlist[:-1]+nlist[1:])/2.0*np.diff(zlist)
dtauhmin=np.outer(n_density,xs_hmin(wvl_))
dtauray=np.outer(n_density,rayscatt(wvl_))

for vmrhmin in range(-14,-8,1):
	for vmrl in tqdm(range(-9,-3,1)):
		for vmr2 in tqdm(range(-9,-3,1)):
			
			dtau1=np.outer(n_density,xs_1)
			dtau2=np.outer(n_density,xs_2)
			
			dtautotal= dtau1*(10**vmrel) + dtau2*(10**vmre2) + dtauhmin*(10**vmrhmin) + dtauray
			
			offset=0
			R0=Rp*const.R_jup.to(u.m).value-offset
			tautilde=[]
			for irt in range(0,len(zlist)-1):
				chordweight=2.0/np.sqrt(1.0-((R0+zlist[irt])/(R0+zlist[1:]))**2)
				tautilde.append(dtautotal[irt:].transpose().dot(chordweight[irt:]))
			tautilde=np.array(tautilde)

			dz=np.diff(zlist)
			zdeltaz=dz*(zcent+R0)
			Rplam2=np.square(R0)+2.0*(1.0 - np.exp(-tautilde)).transpose().dot(zdeltaz)
			Rscgs2= np.square(Rs*const.R_sun.to(u.m).value)
			trspec= 1.0 - Rplam2/Rscgs2
			trspecall.append(trspec)
			
			wvlair=vac2air(wvl_)
			flux=trspec
			stepsize= 0.015
			wvlair_hires=np.arange(wvlair[0],wvlair[-1],stepsize)
			tck=interpolate.splrep(wvlair,flux)
			flx=interpolate.splev(wvlair_hires,tck,der=0)
			
			rflx_hds = pyasl.instrBroadGaussFast(wvlair_hires, flx,115000,edgeHandling='firstlast')
			h5f_spec.create_dataset('spec_'+str(name1)+str(vmr1)+'_'+str(name2)+str(vmr2)+'_hmin'+str(vmrhmin), data=rflx_hds, compression='gzip', compression_opts=9)
h5f_spec.create_dataset('wavelength',data=wvlair_hires, compression='gzip',compression_opts=9)

h5f_spec.close()
h5f_cc.close()
