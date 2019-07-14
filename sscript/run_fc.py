import numpy as np
import os
from tqdm import tqdm
planetname='kelt20b'

for T in tqdm(range(1750,3251,250)):
	input=str(planetname)+'-iso-'+str(T)+'K-fc.tp'
	f=open('input/config.input','w')
	f.write('#FastChem parameter file\n')
	f.write('input/parameters.dat\n')
	f.write('\n')
	f.write('#Atmospheric profile input file\n')
	f.write('input/'+str(input)+'\n')
	f.write('\n')
	f.write('#Abundances output file\n')
	f.write('output/chem_output_'+str(input)+'\n')
	f.write('\n')
	f.write('#Monitor output file\n')
	f.write('output/monitor_output.dat\n')
	f.write('\n')
	f.write('#FastChem console verbose level (1 - 4); 1 = almost silent, 4 = detailed console output\n')
	f.write('4\n')
	f.write('\n')
	f.write('#Output mixing ratios (MR) or particle number densities (ND, default)?\n')
	f.write('MR\n')
	f.close()
	os.system('./fastchem input/config.input >'+str(input[:-2])+'out')
