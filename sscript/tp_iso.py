import numpy as np
import h5py
import os
import astropy.units as u
import astropy.constants as const
from tqdm import tqdm
planetname='kelt20b'
Mp=3.510 #Planet's mass in M jupiter
Rs=1.60  #Stellar's radius in R sun
Rp=1.83  #Planet's radius in R jupiter
mu=2.3   #Jupiter H2-He
Tlow=1750
Thigh=4500
stepT=250

p_lower= 1
p_upper= -8
nlayer= 60
g= const.G.value*Mp* const.M_jup.value/(Rp*const.R_jup.value)**2 # m/s2
k= 0.01*1e-4*1e3 # assumed geometric mean opacity within the white-light bandpass (cm2 g-1)

print ('Isothermal Atmospheric Model')
print ('by Stevanus. K. Nugroho')
print ("Queen's University Belfast")
print ('P0 determination using Heng 2016)
print ('')
print ("Planet's name  = "+str(planetname))
print ('Mp             = '+str(Mp)+" Mj")
print ('Rp             = '+str(Rp)+" Rj")
print ('Rs             = '+str(Rs)+" Rsun")
print ('mu             = '+str(mu))
print ('g              = '+str(g)+' m s-2')
print ('k              = '+str(k)+' cm2 g-1')
print ('')
print ('T isothermal   = '+str(Tlow)+'-'+str(Thigh)+' K')
print ('delta T        = '+str(stepT)+' K')
print ('P_lower-P_upper= '+str(10**p_lower)+' to '+str(10**p_upper)+' bar')
print ('# layer        = '+str(nlayer))
print ('')

for Tiso in tqdm(range(Tlow,Thigh,stepT)):
	P_=np.linspace(p_lower,p_upper,nlayer)
	T_=np.ones(len(P_))*Tiso
	pcent=(P_[1:]+P_[:-1])/2.
	tcent=(T_[1:]+T_[:-1])/2.
	#P_ and T_ are the pressure and the temperature of the boundary of the atmospheric layers
	#pcent and tcent is the pressure and temperature of the atmospheric layers
	pbar=10**P_ #Pressure in bar
		
	nlist=pbar*1e5/const.k_B.value/T_/(1e6) #Ideal gas law, cm-3

	H= (const.k_B.value*T_)/(mu*const.m_p.value*g) # m
			
	P0=0.56*g/k*np.sqrt(H[0]/(2.*np.pi*Rp*const.R_jup.value))/1e5 #bar Heng 2016
	print ('Tiso= '+str(Tiso)+' K')
	print ('P0  = '+str(P0)+' bar')
	zlist= -H*np.log(pbar/P0) # m

	print ('H   ~ '+str(int(np.mean(H/1000)))+' km')
		
		
	tpfile=h5py.File('kelt20b-'+str(Tiso)+'K.prof','w')
	tpfile.create_dataset('P_bound (bar)',data=10**P_)
	tpfile.create_dataset('T_bound (K)',data=T_)
	tpfile.create_dataset('P_layer (bar)',data=10**pcent)
	tpfile.create_dataset('T_layer (K)',data=tcent)
	tpfile.create_dataset('z_bound (K)',data=zlist)

	tpfile.create_dataset('n_density (element.cm-3)',data=nlist)
	tpfile.create_dataset('Mp_Rp_Rs_mu,k,P0',data=np.array([Mp,Rp,Rs,mu,k,P0]))
	tpfile.create_dataset('H (m)',data=H)
	tpfile.close()
	print ('Output file: '+str(planetname)+'-'+str(Tiso)+'K.prof')
	print ('')
