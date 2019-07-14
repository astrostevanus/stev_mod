import numpy as np
import h5py
import os
import argparse

elname=np.array(['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg',
       'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr',
       'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
       'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
       'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
       'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er',
       'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au',
       'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
       'Pa', 'U', 'Np', 'Pu', 'Am', 'Cu', 'Bk', 'Cf', 'Es', 'Fm', 'Md',
       'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn',
       'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo'])
elcode=np.array(['10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200',
       '210', '220', '230', '240', '250', '260', '270', '280', '290',
       '300', '310', '320', '330', '340', '350', '360', '370', '380',
       '390', '400', '410', '420', '430', '440', '450', '460', '470',
       '480', '490', '500', '510', '520', '530', '540', '550', '560',
       '570', '580', '590', '600', '610', '620', '630', '640', '650',
       '660', '670', '680', '690', '700', '710', '720', '730', '740',
       '750', '760', '770', '780', '790', '800', '810', '820', '830',
       '840', '850', '860', '870', '880', '890', '900', '910', '920',
       '930', '940', '950', '960', '970', '980', '990', '1000', '1010',
       '1020', '1030', '1040', '1050', '1060', '1070', '1080', '1090',
       '1100', '1110', '1120', '1130', '1140', '1150', '1160', '1170',
       '1180'])
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HELIOS-K Kurucz Opacity Calculator Assistance, please also check the param.dat for line profile and Units')
    parser.add_argument('-tp', nargs=1, required=True, help='T-P profile filename')    
    parser.add_argument('-wvmin', nargs=1, required=True, help='the minimum wavelength (Angstrom)')
    parser.add_argument('-wvmax', nargs=1, required=True, help='the maximum wavelength (Angsrom)')
    parser.add_argument('-el', nargs=1, required=True, help="element's name")
#    parser.add_argument('-cut', nargs=1, required=True, help="cut limit")
    parser.add_argument('-iso', help='if isothermal T-P profile',action='store_true')
    parser.add_argument('-ion', help='singly ionised',action='store_true')
    
    args = parser.parse_args()
    
    tpfilename, wvmin, wvmax,element= args.tp[0], args.wvmin[0], args.wvmax[0],args.el[0]
    path='./data/kurucz_stev/'
    
    cutMode=int(1) 
    if cutMode==0:
        cutModenote='cut at absolute wavenumbers'
    elif cutMode==1:
        cutModenote='cut at multiple values of Lorentz widths'
    elif cutMode==2:
        cutModenote='cut at multiple values of Doppler widths'
    else:
        print('check the manual please')
        
    cut=1e30 #if cutMode= 0 then the unit is cm-1. 1e30 practically means no cutting
    
    dnu= 0.01 #cm-1 
    
    numin=int(1e8/float(wvmax))
    numax=int(1e8/float(wvmin))
    print ('')
    print ('############################################################')
    print ('')
    print ('Script assistance for HELIOS-K Kurucz Opacity Calculator #')
    print ('by Stevanus. K. Nugroho')
    print ("Queen's University Belfast")
    print ('v1.0 22 May 2019')
    print ('')
    print ('')
    print ('Default value:')
    print ('# Wavenumber resolution: '+str(dnu)+' cm-1')
    print ("# Wing's cut mode      : "+str(cutMode))
    print ("# doResampling and doStoreFullK is on, ")
    print ('')
    print ('')
    #load the tp-profile 
    tpfile=h5py.File(tpfilename,'r')
    tcent=tpfile['T_layer (K)'][:]
#    pcent=tpfile['P_layer (bar)'][:]
    tlist=tpfile['T_bound (K)'][:]
    zlist=tpfile['z_bound (K)'][:]
    tpfile.close()

    
    #ionised or not
    if args.ion:
        state=1
        statenote='II'
    else:
        state=0
        statenote='I'
    print ('T-P profile name      : '+str(tpfilename))
    print ('Element               : '+str(element)+' '+str(statenote))
    print ('Wavelength range      : '+str(wvmin)+'-'+str(wvmax)+' Angstrom')
    print ('Cut limit             : '+str(cut))
    #element filename
    for i in range(len(elname)):
        if element==elname[i]:
            if i+1<10:
                 molid='gfnew0'+str(elcode[i])+str(state)
            else:
                 molid='gfnew'+str(elcode[i])+str(state)
    if args.iso:
        os.system('./heliosk -name '+str(tpfilename[:-5])+'_'+str(element)+'_'+str(statenote)+' -T '+str(tlist[0])+' -P 0.01 -M '+str(molid)+' -numin '+str(numin)+' -numax '+str(numax)+' -path '+str(path)+' -cut '+str(cut)+' -dnu '+str(dnu))
    else:
        for i in tqdm(range(len(tlist))):
            os.system('./heliosk -name '+str(tpfilename[:-5])+'_'+str(element)+'_'+str(statenote)+'_'+str(i+1)+' -T '+str(tlist[i])+' -P 0.01 -M '+str(molid)+' -numin '+str(numin)+' -numax '+str(numax)+' -path '+str(path)+' -cut '+str(cut)+' -dnu'+str(dnu))
