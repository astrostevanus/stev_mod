import warnings
warnings.filterwarnings("ignore")
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
fc_dict= np.array(['P(bar)', 'T(k)', 'n_<H>(cm-3)','n_g(cm-3)','m(u)', 'e-', 'Al_I', 'Ar_I', 'C_I', 'Ca_I',
				   'Cl_I', 'Co_I', 'Cr_I', 'Cu_I', 'F_I', 'Fe_I', 'Ge_I', 'H_I', 'He_I', 'K_I', 'Mg_I', 'Mn_I',
				   'N_I', 'Na_I', 'Ne_I', 'Ni_I', 'O_I', 'P_I', 'S_I', 'Si_I', 'Ti_I', 'V_I', 'Zn_I', 'Al1Cl1',
				   'Al1Cl1F1', 'Al1Cl1F2', 'Al1Cl1O1', 'Al1Cl2', 'Al1Cl2F1', 'Al1Cl3', 'Al1F1', 'Al1F1O1', 'Al1F2',
				   'Al1F2O1', 'Al1F3', 'Al1F4Na1', 'Al1H1', 'Al1H1O1_1','Al1H1O1_2','Al1H1O2', 'Al1N1', 'Al1O1',
				   'Al1O2', 'Al1S1', 'Al2', 'Al2Cl6', 'Al2F6', 'Al2O1', 'Al2O2', 'C1Al1', 'C1Cl1', 'C1Cl1F1O1',
				   'C1Cl1F3', 'C1Cl1N1', 'C1Cl1O1', 'C1Cl2', 'C1Cl2F2', 'C1Cl2O1', 'C1Cl3', 'C1Cl3F1', 'C1Cl4',
				   'C1F1', 'C1F1N1', 'C1F1O1', 'C1F2', 'C1F2O1', 'C1F3', 'C1F4', 'C1F4O1', 'C1F8S1', 'C1H1',
				   'C1H1Cl1', 'C1H1Cl3', 'C1H1F1', 'C1H1F1O1', 'C1H1F3', 'C1H1N1', 'C1H1N1O1', 'C1H1O1', 'C1H1P1',
				   'C1H2', 'C1H2Cl2', 'C1H2Cl1F1','C1H2F2', 'C1H2O1', 'C1H3', 'C1H3Cl1', 'C1H3F1', 'C1H4', 'C1K1N1',
				   'C1N1', 'C1N1Na1', 'C1N1O1', 'C1N2_cnn', 'C1N2_ncn', 'C1O1', 'C1O1S1', 'C1O2', 'C1P1', 'C1S1',
				   'C1S2', 'C1Si1', 'C1Si2', 'C2', 'C2Cl2', 'C2Cl4', 'C2Cl6', 'C2Cr1', 'C2F2', 'C2F3N1', 'C2F4',
				   'C2F6', 'C2H1', 'C2H1Cl1', 'C2H1F1', 'C2H2', 'C2H4', 'C2H4O1', 'C2K2N2', 'C2N1', 'C2N2',
				   'C2N2Na2', 'C2Si1', 'C2Si2', 'C2O1', 'C2Ti1', 'C2V1', 'C3', 'C3H1', 'C3O2', 'C4', 'C4N2',
				   'C4Ni1O4', 'C4Ti1', 'C4V1', 'C5', 'C5Fe1O5', 'Ca1Cl1', 'Ca1Cl2', 'Ca1F1', 'Ca1F2', 'Ca1H1',
				   'Ca1H1O1', 'Ca1H2O2', 'Ca1O1', 'Ca1S1', 'Ca2', 'Cl1Co1', 'Cl1Cu1', 'Cl1F1', 'Cl1F1Mg1',
				   'Cl1F1O2S1','Cl1F1O3', 'Cl1F2O1P1','Cl1F3', 'Cl1F3Si1', 'Cl1F5', 'Cl1F5S1', 'Cl1Fe1',
				   'Cl1H1', 'C1H1Cl1F2','C1H1Cl2F1','Cl1H1O1', 'Cl1H3Si1', 'Cl1K1', 'Cl1Mg1', 'Cl1N1O1',
				   'Cl1N1O2', 'Cl1Na1', 'Cl1Ni1', 'Cl1O1', 'Cl1O1Ti1', 'Cl1O2', 'Cl1O3', 'Cl1P1', 'Cl1S1',
				   'Cl1S2', 'Cl1Si1', 'Cl1Ti1', 'Cl2', 'Cl2Co1', 'Cl2F1O1P1','Cl2Fe1', 'Cl2H2Si1', 'Cl2K2',
				   'Cl2Mg1', 'Cl2Na2', 'Cl2Ni1', 'Cl2O1_clocl','Cl2O1_clclo','Cl2O1Ti1',
				   'Cl2O2_clo2cl','Cl2O2_cloclo','Cl2O2S1', 'Cl2S1', 'Cl2Si1', 'Cl2Ti1',
				   'Cl3Co1', 'Cl3Cu3', 'Cl3F1Si1', 'Cl3Fe1', 'Cl3H1Si1', 'Cl3O1P1', 'Cl3P1',
				   'Cl3P1S1', 'Cl3Si1', 'Cl3Ti1', 'Cl4Co2', 'Cl4Fe2', 'Cl4Mg2', 'Cl4Si1', 'Cl4Ti1',
				   'Cl5P1', 'Cl6Fe2', 'Co1F2', 'Cr1H1', 'Cr1N1', 'Cr1O1', 'Cr1O2', 'Cr1O3', 'Cu1F1', 'Cu1F2',
				   'Cu1H1', 'Cu1O1', 'Cu1S1', 'Cu2', 'F1Fe1', 'F1H1', 'F1H1O1', 'F1H1O3S1', 'F1H3Si1', 'F1K1',
				   'F1Mg1', 'F1N1', 'F1N1O1', 'F1N1O2', 'F1N1O3', 'F1Na1', 'F1O1', 'F1O1Ti1', 'F1O2_ofo',
				   'F1O2_foo', 'F1P1', 'F1P1S1', 'F1S1', 'F1Si1', 'F1Ti1', 'F2', 'F2Fe1', 'F2H2', 'F2H2Si1',
				   'F2K2', 'F2Mg1', 'F2N1', 'F2N2cis', 'F2N2trans','F2Na2', 'F2O1', 'F2O1S1', 'F2O1Si1', 'F2O1Ti1',
				   'F2O2', 'F2O2S1', 'F2P1', 'F2S1', 'F2S2_1', 'F2S2_2', 'F2Si1', 'F2Ti1', 'F3Fe1', 'F3H1Si1',
				   'F3H3', 'F3N1', 'F3N1O1', 'F3O1P1', 'F3P1', 'F3P1S1', 'F3S1', 'F3Si1', 'F3Ti1', 'F4H4', 'F4Mg2',
				   'F4N2', 'F4S1', 'F4Si1', 'F4Ti1', 'F5H5', 'F5P1', 'F5S1', 'F6H6', 'F6S1', 'F7H7', 'F10S2',
				   'Fe1H2O2', 'Fe1O1', 'Fe1S1', 'H1K1', 'H1K1O1', 'H1Mg1', 'H1Mg1O1', 'H1Mn1', 'H1N1', 'H1N1O1',
				   'H1N1O2cis','H1N1O2trans','H1N1O3', 'H1Na1', 'H1Na1O1', 'H1Ni1', 'H1O1', 'H1O2', 'H1P1', 'H1S1',
				   'H1Si1', 'H2', 'H2K2O2', 'H2Mg1O2', 'H2N1', 'H2N2', 'H2Na2O2', 'H2O1', 'H2O2', 'H2O4S1', 'H2P1',
				   'H2S1', 'H2Si1', 'H3N1', 'H3P1', 'H3Si1', 'H4N2', 'H4Si1', 'K1O1', 'K2', 'K2O4S1', 'Mg1N1',
				   'Mg1O1', 'Mg1S1', 'Mg2', 'Mn1O1', 'Mn1S1', 'N1O1', 'N1O2', 'N1O3', 'N1P1', 'N1S1', 'N1Si1',
				   'N1Si2', 'N1Ti1', 'N1V1', 'N2', 'N2O1', 'N2O3', 'N2O4', 'N2O5', 'N3', 'Na1O1', 'Na2',
				   'Na2O4S1', 'Ni1O1', 'Ni1S1', 'O1P1', 'O1S1', 'O1S2', 'O1Si1', 'O1Ti1', 'O1V1', 'O2', 'O2P1',
				   'O2S1', 'O2Si1', 'O2Ti1', 'O2V1', 'O3', 'O3S1', 'O6P4', 'O10P4', 'P1S1', 'P2', 'P4', 'P4S3',
				   'S1Si1', 'S1Ti1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Si2', 'Si3', 'Al_II', 'Al1-',
				   'Al1Cl_II', 'Al1Cl1F_II','Al1Cl2+', 'Al1Cl2-', 'Al1F_II', 'Al1F2+', 'Al1F2-', 'Al1F2O1-',
				   'Al1F4-', 'Al1H1O_II', 'Al1H1O1-', 'Al1O_II', 'Al1O1-', 'Al1O2-', 'Al2O_II', 'Al2O2+', 'Ar_II',
				   'C_II', 'C1-', 'C1F_II', 'C1F2+', 'C1F3+', 'C1H_II', 'C1H1-', 'C1H1O_II', 'C1N_II', 'C1N1-',
				   'C1O2-', 'C2-', 'Ca_II', 'Ca1H1O_II', 'Cl_II', 'Cl1Mg_II', 'Cl1S_II', 'Cl1-', 'Cl2S_II',
				   'Co_II', 'Co1-', 'Cr_II', 'Cr1-', 'Cu_II', 'Cu1-', 'F_II', 'F1-', 'F1Mg_II', 'F1P_II',
				   'F1P1-', 'F1S_II', 'F1S1-', 'F2K1-', 'F2Mg_II', 'F2Na1-', 'F2P_II', 'F2P1-', 'F2S_II',
				   'F2S1-', 'F3S_II', 'F3S1-', 'F4S_II', 'F4S1-', 'F5S_II', 'F5S1-', 'F6S1-', 'Fe_II', 'Fe1-',
				   'H_II', 'H1-', 'H1K1O_II', 'H1Mg1O_II', 'H1Na1O_II', 'H1O_II', 'H1O1-', 'H1S1-', 'H1Si_II',
				   'H2+', 'H2-', 'H3O_II', 'He_II', 'K_II', 'K1-', 'K1O1-', 'Mg_II', 'Mn_II', 'N_II', 'N1-',
				   'N1O_II', 'N1O2-', 'N2+', 'N2-', 'N2O_II', 'Na_II', 'Na1-', 'Na1O1-', 'Ne_II', 'Ni_II',
				   'Ni1-', 'O_II', 'O1-', 'O2+', 'O2-', 'P_II', 'P1-', 'S_II', 'S1-', 'Si_II', 'Si1-', 'Ti_II',
				   'Ti1-', 'V_II', 'V1-', 'Zn_II', 'Zn1-'])

for t in range(2000,3600,500):
	planetname='kelt20b'
	#kelt20b-iso-3500K-ex.prof
	tpfilename=str(planetname)+'-iso-'+str(t)+'K-ex.prof'
	tpfile=h5py.File(tpfilename,'r')
	tcent=tpfile['T_layer (K)'][:]
	pcent=tpfile['P_layer (bar)'][:]
	tlist=tpfile['T_bound (K)'][:]
	zlist=tpfile['z_bound (m)'][:]
	zcent=(zlist[1:]+zlist[:-1])/2.
	nlist=tpfile['n_density (element.cm-3)'][:]
	Mp,Rp,Rs,mu,k,P0=tpfile['Mp_Rp_Rs_mu,k,P0'][:]
	tpfile.close()
	print (len(nlist))
	#name=np.array(['Na_I','Fe_I','Fe_II','Ti_I','Ti_II','Mg_I','Cr_II','Sc_II','Y_II','Ca_I','Ca_II','Cr_I','Co_I','Sr_II'])
	name=np.array(['Ca_I','Ca_II','Fe_I','Fe_II','Mg_I','Na_I','Ti_I','Ti_II'])

	h5f_specharpsn=h5py.File(str(tpfilename[:-5])+'-trans-kurucz-detected-fc.h5', 'w')
	h5f_speccarmenes=h5py.File(str(tpfilename[:-5])+'-trans-kurucz-detected-fc-carmenes.h5', 'w')

	h5f_cc=h5py.File('xs-'+str(t)+'K-kurucz.h5', 'r')

	fc_vmr=np.loadtxt('../FastChem/output/chem_output_'+tpfilename[:-5]+'-fc.tp',comments='#')


	nH_1=np.arange(len(fc_dict))[fc_dict=='H1-'][0]
	nH2=np.arange(len(fc_dict))[fc_dict=='H2'][0]

	vmrhmin=fc_vmr[:,nH_1]
	vmrh2=fc_vmr[:,nH2]
	n_density=(nlist[:-1]+nlist[1:])/2.0*np.diff(zlist)*100.
	
	dtauhmin=np.outer(n_density*vmrhmin,xs_hmin(wvl_))
	dtauray=np.outer(n_density*vmrh2,rayscatt(wvl_))
	
	dtauel=[]
	for i in tqdm(range(len(name))):
		n_el=np.arange(len(fc_dict))[fc_dict==name[i]][0]
		spec=h5f_cc["spec_"+str(name[i])][:]
		wvl_,xs_=spec[0],spec[1]
	
		vmr_el=fc_vmr[:,n_el]
		
		dtauel.append(np.outer(n_density*vmr_el,xs_))
	dtau_el=np.sum(dtauel,axis=0)
		
		
	dtautotal=dtau_el*+dtauhmin+dtauray
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

	wvlair=vac2air(wvl_)
	flux=trspec
	stepsize= 0.015
	wvlair_hires=np.arange(wvlair[0],wvlair[-1],stepsize)
	tck=interpolate.splrep(wvlair,flux)
	flx=interpolate.splev(wvlair_hires,tck,der=0)

	rflx_hds = pyasl.instrBroadGaussFast(wvlair_hires, flx,115000,edgeHandling="firstlast")
	rflx_hdscar = pyasl.instrBroadGaussFast(wvlair_hires, flx,94600,edgeHandling="firstlast")
	
	h5f_specharpsn.create_dataset("spec_"+str(t)+"K",data=rflx_hds, compression="gzip",compression_opts=9)
	h5f_speccarmenes.create_dataset("spec_"+str(t)+"K",data=rflx_hdscar, compression="gzip",compression_opts=9)

	h5f_specharpsn.create_dataset("wavelength",data=wvlair_hires, compression="gzip",compression_opts=9)
	h5f_speccarmenes.create_dataset("wavelength",data=wvlair_hires, compression="gzip",compression_opts=9)

	h5f_specharpsn.close()
	h5f_speccarmenes.close()
	h5f_cc.close()
