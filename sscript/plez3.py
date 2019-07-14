import numpy as np
import math
import struct
import os
import argparse
from astropy import constants as const
from astropy import units as u
from scipy import interpolate
from tqdm import tqdm
# This script download Plez TiO and VO line list and produces the binary and *.param files for HELIOS-K
# Date: May 2019
# Author: Stevanus Kristianto Nugroho
# Email: s.nugroho@qub.ac.uk
# Based on Kurucz2.py in HELIOS-K


eesu=const.e.esu #electron charge in cgs units
ee=(eesu*eesu).value #
me=const.m_e.cgs.value #mass of electron
c=const.c.cgs.value #speed of light in cm/s
h=const.h.cgs.value #planck constant
k=const.k_B.cgs.value #boltzmann constant

def vac2air(wv_vac):
	s = 1e4 /wv_vac
	n = 1.+0.0000834254+0.02406147/(130.-s**2)+0.00015998/(38.9-s**2)
	wv_air=wv_vac/n
	return wv_air

#choose if the file contains wavenumber or not
theo=1

massplez=[61.947543,62.946663, 63.942857, 64.942780,65.939702, 66.938871]
isotope=[0.0825,0.0744,0.7392,0.0541,0.0518, 0.9975]
files=['linelist_reduced46_all_deltacorr.dat.gz', 'linelist_reduced47_all_deltacorr.dat.gz', 'linelist_reduced48_all_deltacorr_lab.dat.gz','linelist_reduced49_all_deltacorr.dat.gz','linelist_reduced50_all_deltacorr.dat.gz','linelistVO_ALL.dat.gz']

def main(name):
	if name=='TiO':
#		for iso in range(46,51):
#			os.system('wget https://nextcloud.lupm.in2p3.fr/s/r8pXijD39YLzw5T/download?path=%2FTiOVALD&files='+str(files[iso-46]))
#			os.system('tar xvzf '+str(files[iso-46]))
		for iso in range(46,51):
			processLineList(name,iso)
	elif name=='VO':
#		os.system('wget https://nextcloud.lupm.in2p3.fr/s/r8pXijD39YLzw5T/download?path=%2FVO&files='+str(files[-1]))
		processLineList(name,'51')

def processLineList(name,iso):
	outname = str(iso)+str(name)+"-plez"+str(theo)+".bin"
	pfname = str(iso)+str(name)+"-plez"+str(theo)+".pf"
	mass = massplez[iso-46]
	filename=files[iso-46][:-3]

	

	if name=='TiO':
		os.system('cp ./data/exomol/'+str(iso)+'Ti-16O__Toto.pf '+str(pfname))
	elif name=='VO':
		os.system('cp ./data/exomol/51V-16O__VOMYT.pf '+str(pfname))

	temp,q_t=np.loadtxt(pfname,unpack=True)
    
	QT0= interpolate.interp1d(temp,q_t,kind="cubic")(296.0)
        
	output_file = open(outname,"wb")
	nl=0
	with open(filename,'r') as f:
		lambair=[]
		gf=[]
		Elow=[]
		Jl=[]
		Eup=[]
		GammaR=[]
		for r in f.readlines():
			nl = nl + 1
			lambair.append(float(r[0:14]))
			gf.append(float(r[15:27]))
			Eu=np.abs(float(r[58:71]))
			Elo=np.abs(float(r[28:39]))
			Jl.append(float(r[44:50]))

			if Elo>Eu:
				Elow.append(Eu)
				Eup.append(Elo)
			else:
				Elow.append(Elo)
				Eup.append(Eu)
			GammaR.append(float(r[90:103]))

		lambair=np.array(lambair,dtype="f4")
		gf=np.array(gf,dtype="f4")
		Elow=np.array(Elow,dtype="f4")
		Jl=np.array(Jl,dtype="f4")
		Eup=np.array(Eup,dtype="f4")
		GammaR=np.array(GammaR,dtype="f4")

		if(theo == 1):
			wn = Eup-Elow
		#wlvac = 1e8/wn
		#wl=vac2air(wlvac)   #in angstrom
		else:
			s = 10000.0 / lambair
			n = 1.0 + 0.00008336624212083 + 0.02408926869968 / (130.1065924522 - s*s) + 0.0001599740894897 / (38.92568793293 - s*s)
			wl = lambair*n #in angstrom
			wn=1e8/wl
		
#S=linestrength_hitran_zero(gf,Elow,wn,QT0)*cons.t.N_A.value/mass*isotope[iso-46]
		S = np.pi * ee * gf * cons.t.N_A.value / (c * c * me * mass)#*isotope[iso-46]
	
		ind=np.argsort(wn)
		wn=wn[ind]
		S=S[ind]
		Elow=Elow[ind]
		GammaR=0.5*GammaR[ind]
		print('Saving in binary file')
		
		for i in tqdm(range(len(wn))):
			s = struct.pack('d', np.float128(wn[i]))
			output_file.write(s)
			s = struct.pack('d', np.float128(S[i]))
			output_file.write(s)
			s = struct.pack('d', np.float128(Elow[i]))
			output_file.write(s)
			s = struct.pack('d', 0.0)
			output_file.write(s)
			s = struct.pack('d', np.float128((GammaR[i])))
			output_file.write(s)
	numax=int(np.max(wn))
	print("Output: "+str(outname)+"\n")
	print("#Lines: "+str(nl)+"\n")

	output_file.close()

	printCode = 1
	if(nl > 0 and printCode == 1):
		f = open(str(iso)+str(name)+"-plez"+str(theo)+".param",'w')
		print("Database = 30", file = f)
		print("Molecule number = 81", file = f)
		print("Name = "+str(iso)+str(name)+"-plez"+str(theo), file = f)
		print("Number of Isotopes = 1", file = f)
		print("#Id Abundance      Q(296K)   g     Molar Mass(g)  partition file :", file = f)
		print(" 0     1         "+str(QT0)+"       0      "+str(mass)+"        "+str(pfname), file = f)
		print("Number of columns in partition File = 2", file = f)
		print("Number of line/transition files = 1", file = f)
		print("Number of lines per file :", file = f)
		print("%d" % nl, file = f)
		print("Line file limits :", file = f)
		print("0", file = f)
		print(str(int(numax)), file = f)
		print("#ExoMol :", file = f)
		print("Number of states = 0", file = f)
		print("Number of columns in transition files = 0", file = f)
		print("Default value of Lorentzian half-width for all lines = 0.0", file = f)
		print("Default value of temperature exponent for all lines = 0.0", file = f)
		print("Version = %s" % filename, file = f)

		f.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Convert Plez's Linelist to HELIOS-K's Binary Files")
	parser.add_argument('-mol', nargs=1, help='TiO/VO?',type=str)
	args = parser.parse_args()
	name=args.mol[0]
	print("")
	print("Converting Plez's "+str(name)+" line list to HELIOS-K's Binary Files")
	main(name)
