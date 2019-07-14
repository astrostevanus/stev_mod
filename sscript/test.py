import os 
import numpy as np
element=np.array(['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg',
       'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr',
       'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
       'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
       'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
       'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er',
       'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt'])
#element=np.array(['K','Mg'])
#for t in range(2000,4600,500):
t=2500
for i in range(len(element)):
    os.system('python op_kurucz.py -tp kelt20b-'+str(t)+'K.prof -wvmin 3000 -wvmax 9600 -el '+str(element[i])+' -iso ')
    os.system('python op_kurucz.py -tp kelt20b-'+str(t)+'K.prof -wvmin 3000 -wvmax 9600 -el '+str(element[i])+' -iso -ion')
