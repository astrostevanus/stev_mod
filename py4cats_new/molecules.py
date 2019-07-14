#!/usr/bin/env python3
"""  molecules

  A module essentially defining/collecting molecular data (mass, ...)
  and the ID numbers used by spectroscopic data bases (Hitran, Geisa, ...)

  Usage as a command line script:

    molecules [options] [species]

    without argument:         list known molecules along with 'main' data
    with molecular name(s):   list all attributes of this molecule(s)
    with option -s:           -sh  sort according to hitran id number
                              -sg  sort according to geisa  id number
                              -sm  sort according to molecular mass
                              -sn  sort according to molecular name

  A dictionary of dictionaries containing molecular data along with some convenience functions.

  NOTE:  HDO  is considered as an individual molecule in GEISA2015
         CH3D is separate from CH4 in GEISA 2008 ff
"""

##############################################################################################################
#####  LICENSE issues:                                                                                   #####
#####                 This file is part of the Py4CAtS package.                                          #####
#####                 Copyright 2002 - 2019; Franz Schreier;  DLR-IMF Oberpfaffenhofen                   #####
#####                 Py4CAtS is distributed under the terms of the GNU General Public License;          #####
#####                 see the file ../license.txt in the parent directory.                               #####
##############################################################################################################

### L.A. Pugh and K.N. Rao: "Intensities from Infrared Spectra" in Rao (ed.): Molecular Spectroscopy: Modern Research (1976)
### M.A. Smith et al.: "Intensities and Collision Broadening Parameters from Infrared Spectra" in Rao (ed.) 1985
### see also:
### http://vpl.astro.washington.edu/spectra/fundamentals.htm

# NOTE: Some entries have been renamed: 'Omega' ---> 'VibFreq' (relative to Fortran)

molecules = {
 'H2O': {'hitran': 1,
         'geisa': 1,
	 'sao': 1,
	 'jpl':18,
         'isotopes': ['161', '181', '171', '162', '182', '172', '272', '282'],
         'mass':    18.0150,
         'TempExpQR':    1.50000,
         'TempExpGL':   0.500000,
         'VibFreq': [    3657.00,    1595.00,    3756.00],
         'NumDeg': [  1,  1,  1]
 },

 'HDO': {#'hitran': 1,
         'geisa': 51,
	 'sao': 1,
         'isotopes': ['162', '172', '182'],  # order as given by GEISA2015 @ ether
         'mass':    19.0150,
         'TempExpQR':    1.50000,
         'TempExpGL':   0.500000,
         'VibFreq': [    2724.00,    1403.00,    3707.00],  # data from Smith85 in Rao: Molecular Spectroscopy: Modern Research (1985)
         'NumDeg': [  1,  1,  1]
 },

 'CO2': {'hitran': 2,
         'geisa': 2,
         'sao': 2,
         'isotopes': ['626', '636', '628', '627', '638', '637', '828', '827', '727', '838'],  # HITRAN 2012ff
         #           ['626', '636', '628', '627', '638', '637', '828', '728', '727', '838'],  # HITRAN 2004
         'mass':    44.0100,
         'TempExpQR':    1.00000,
         'TempExpGL':   0.750000,
         'VibFreq': [    1388.00,    667.000,    2349.00],
         'NumDeg': [  1,  2,  1]
 },

'O3':   {'hitran': 3,
         'geisa': 3,
         'sao': 3,
         'jpl': 48,
         'isotopes': ['666', '668', '686'],
         'mass':    47.9980,
         'TempExpQR':    1.5000,
         'TempExpGL':   0.750000,
         'VibFreq': [    1103.00,    701.000,    1042.00],
         'NumDeg': [  1,  1,  1]
 },

'N2O': {'hitran': 4,
        'geisa': 4,
	'sao': 4,
	'jpl': 44,
        'isotopes': ['446', '456', '546', '448', '447'],
        'mass':    44.0100,
        'TempExpQR':    1.00,
        'TempExpGL':   0.750000,
        'VibFreq': [    2224.00,    589.000,    1285.00],
        'NumDeg': [  1,  2,  1]
 },

'CO': {'hitran': 5,
       'geisa': 5,
       'sao': 5,
       'isotopes': ['26', '36', '28', '27', '38'],
       'mass':    28.0110,
       'TempExpQR':    1.00,
       'TempExpGL':   0.750000,
       'VibFreq': [    2143.00],
       'NumDeg': [  1]
 },

'CH4': {'hitran': 6,
        'geisa': 6,
        'sao': 6,
        'isotopes': ['211', '311', '212', '312'],
        'mass':    16.0430,
        'TempExpQR':    1.50,
        'TempExpGL':   0.750000,
        'VibFreq': [    2917.00,    1533.00,    3019.00,    1311.00],
        'NumDeg': [  1,  2,  3,  3  ]
 },
'CH3D': {'geisa': 23,
         'mass':    17.0430,
         'isotopes': ['212', '312'],
         'TempExpQR':    1.50,
         'TempExpGL':   0.750000,
         'VibFreq': [    2917.00,    1533.00,    3019.00,    1311.00],
         'NumDeg': [  1,  2,  3,  3  ]
 },

'O2': {'hitran': 7,
       'geisa': 7,
       'sao': 7,
       'jpl': 32,
       'isotopes': ['66', '68', '67'],
       'mass':    31.9990,
       'TempExpQR':    1.00,
       'TempExpGL':   0.500000,
       'VibFreq': [    1556.00],
       'NumDeg': [  1],
 },

'NO': {'hitran': 8,
       'geisa': 8,
       'sao': 8,
       'isotopes': ['46', '56',  '48'],
       'mass':    30.0100,
       'TempExpQR':    1.22450,
       'TempExpGL':   0.500000,
       'VibFreq': [    1876.00],
       'NumDeg': [  1]
 },

'SO2': {'hitran':9,
        'geisa': 9,
        'sao': 9,
        'isotopes': ['626', '646'],
        'mass':    64.0600,
        'TempExpQR':    1.50,
        'TempExpGL':   0.500000,
        'VibFreq': [    1152.00,    518.000,    1362.00],
        'NumDeg': [  1,  1,  1 ]
 },

'NO2': {'hitran':10,
        'geisa':10,
        'sao':10,
        'isotopes': ['646'],
        'mass':    46.0100,
        'TempExpQR':    1.50,
        'TempExpGL':   0.500000,
        'VibFreq': [    1320.00,    750.000,    1617.00],
        'NumDeg': [  1,  1,  1]
 },

'NH3': {'hitran':11,
        'geisa':11,
        'sao':11,
        'isotopes': ['4111', '5111'],
        'mass':    17.0300,
        'TempExpQR':    1.50000,
        'TempExpGL':   0.500000,
        'VibFreq': [    3337.00,    950.000,    3444.00,    1630.00],
        'NumDeg': [  1,  1,  1,  2]
 },

'HNO3':  {'hitran':12,
          'geisa':13,
          'sao':12,
          'jpl': 63,
          'isotopes': ['146'],
          'mass':    63.0100,
          'TempExpQR':    1.50,
          'TempExpGL':   0.500000,
          'VibFreq': [ 3350.00, 1710.00,  1326.00,  1304.00, 879.00,  647.00,   580.00,   763.000,  458.000],
          'NumDeg': [  1,  1,  1,  1, 1,  1,  1,  1,  1]
 },

'OH':  {'hitran':13,
        'geisa':14,
        'sao':13,
        'isotopes': ['61', '81', '62'],
        'mass':    17.0000,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    3570.00],
        'NumDeg': [  1]
 },

'HF':  {'hitran':14,
        'geisa':15,
        'sao':14,
        'isotopes': ['19'],
        'mass':    20.0100,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    3961.00],
        'NumDeg': [  1 ]
 },

'HCl': {'hitran':15,
        'geisa':16,
        'sao':15,
        'isotopes': ['15', '17'],
        'mass':    36.4600,
        'TempExpQR':    1.00,
        'TempExpGL':   0.750000,
        'VibFreq': [    2886.00],
        'NumDeg': [  1]
 },

'HBr': {'hitran':16,
        'geisa':17,
        'sao':16,
        'isotopes': ['19', '11'],
        'mass':    80.9200,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    2559.00],
        'NumDeg': [  1]
 },

'HI':  {'hitran':17,
        'geisa':18,
        'sao':17,
        'isotopes': ['17'],
        'mass':    127.910,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    2230.00],
        'NumDeg': [  1]
 },

'ClO': {'hitran':18,
        'geisa':19,
        'sao':18,
        'jpl': 52,
        'isotopes': ['56', '76'],
        'mass':    51.4500,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    842.000],
        'NumDeg': [  1]
 },

'OCS':  {'hitran':19,
         'geisa':20,
         'sao':19,
         'isotopes': ['622', '624', '632', '822'],
         'mass':    60.0800,
         'TempExpQR':    1.00,
         'TempExpGL':   0.500000,
         'VibFreq': [    859.000,    520.000,    2062.00],
         'NumDeg': [  1,  2,  1]
 },

'H2CO': {'hitran':20,
         'geisa':21,
         'sao':20,
         'isotopes': ['126', '136', '128'],
         'mass':    30.0300,
         'TempExpQR':    1.50,
         'TempExpGL':   0.500000,
         'VibFreq': [  2782.0,  1746.0,  1500.0,  1167.0,  2843.0,  1249.0],
         'NumDeg': [  1,  1,  1,  1,  1,  1  ]
 },

'HOCl': {'hitran':21,
         'geisa':32,
         'sao':21,
         'isotopes': ['165', '167'],
         'mass':    52.4600,
         'TempExpQR':    1.50,
         'TempExpGL':   0.500000,
         'VibFreq': [    3609.00,    1239.00,    724.000],
         'NumDeg': [  1,  1,  1]
 },

'N2':  {'hitran':22,
        'geisa':33,
        'sao':22,
        'isotopes': ['44', '45'],
        'mass':    28.0140,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    2330.00],
        'NumDeg': [  1]
 },

'HCN': {'hitran':23,
        'geisa':27,
        'sao':23,
        'isotopes': ['124', '134', '125'],
        'mass':    27.0300,
        'TempExpQR':    1.00,
        'TempExpGL':   0.500000,
        'VibFreq': [    2097.00,    713.000,    3311.00],
        'NumDeg': [  1,  2,  1]
 },

'CH3Cl': {'hitran':24,
          'geisa':34,
          'sao':24,
          'isotopes': ['215', '217'],
          'mass':    50.4900,
          'TempExpQR':    1.50,
          'TempExpGL':   0.500000,
          'VibFreq': [  2968.0,  1355.0,  733.00,  3039.0,  1452.0,  1018.0],
          'NumDeg': [  1,  1,  1,  2,  2,  2  ]
 },

'H2O2': {'hitran':25,
         'geisa':35,
         'sao':25,
         'isotopes': ['1661'],
         'mass':    34.0100,
         'TempExpQR':    2.00,
         'TempExpGL':   0.500000,
         'VibFreq': [    3607.00,  1394.00,   863.00,  3608.00,   1266.00],
         'NumDeg': [  1,  1,  1,  1,  1]
 },

'C2H2': {'hitran':26,
         'geisa':24,
         'sao':26,
         'isotopes': ['1221', '1231','1222'],
         'mass':    26.0300,
         'TempExpQR':    1.00,
         'TempExpGL':   0.750000,
         'VibFreq': [    3374.00,  1974.00,  3289.00,  629.00,  730.00],
         'NumDeg': [  1,  1,  1,  2,  2]
 },

'C2H6': {'hitran':27,
         'geisa':22,
         'sao':27,
         'isotopes': ['1221', '1231'],
         'mass':    30.0700,
         'TempExpQR':    1.90,
         'TempExpGL':   0.750000,
         'VibFreq': [  2899.00,  1375.00,  993.000,  275.000, 2954.00,  1379.00, 2994.00, 1486.00, 822.000],
         'NumDeg': [  1,  1,  1,  1,  1,  1,  2,  1,  2]
 },

'PH3': {'hitran':28,
         'geisa':12,
         'sao':28,
         'isotopes': ['1111'],
         'mass':    34.0000,
         'TempExpQR':    1.00,
         'TempExpGL':   0.500000,
         'VibFreq': [    2327.00,    992.000,    1118.00,    2421.00],
         'NumDeg': [  1,  1,  2,  2 ]
 },

'COF2': {'hitran':29,
         'geisa':38,
         'isotopes': ['269', '369'],
         'mass':    66.0000,
         'TempExpQR':    1.50,
         'TempExpGL':   0.500000,
         'VibFreq': [    1944.0,  963.00,  582.00,  1242.0,  619.00,  774.00],
         'NumDeg': [  1,  1,  1,  1, 1,  1]
 },

'SF6': {'hitran':30,
         'geisa':39,
         'isotopes': ['29'],
         'mass':    146.000,
         'TempExpQR':    1.50,
         'TempExpGL':   0.647000,
         'VibFreq': [  774.00,  642.00,  948.00,  615.00,  523.00,  346.00],
         'NumDeg': [  1,  2,  3,  3,  3,  3 ]
 },

'H2S': {'hitran':31,
         'geisa':36,
         'isotopes': ['121', '141', '131'],
         'mass':    34.0000,
         'TempExpQR':    1.50,
         'TempExpGL':   0.500000,
         'VibFreq': [    2615.00,    1183.00,    2626.00],
         'NumDeg': [  1,  1,  1]
 },

'HCOOH': {'hitran':32,
          'geisa':37,
          'isotopes': ['126'],
          'mass':    46.00548,
          'TempExpQR':    1.50,
          'TempExpGL':   0.500000,
          'VibFreq': [ 3570.00,  2943.00,  1770.00,  1387.00, 1229.00,  1105.00,  625.000,  1033.00,  638.000],
          'NumDeg': [  1,  1,  1,  1, 1,  1,  1,  1,  1]
 },

'HO2': {'hitran':33,
        'geisa':41,
        'sao':32,
        'isotopes': ['166'],
        'mass':    33.0000,
        'TempExpQR':    1.50,
        'TempExpGL':   0.500000,
        'VibFreq': [    3436.00,    1392.00,    1098.00],
        'NumDeg': [  1,  1,  1]
 },

'ClOOCl': {'mass':    102.0000,
           'TempExpQR':    1.50,
           'TempExpGL':   0.500000,
           'VibFreq': [   127.0, 328.0, 443.0, 560.0, 653.0, 752.0],
           'NumDeg': [  1, 1, 1]
 },

'O':      {'hitran':34,
           'mass':    16.0
 },

'ClONO2': {'hitran':35,
           'geisa':42,
           'mass':    97.5000,
           'TempExpQR':    1.50,
           'TempExpGL':   0.500000,
           'VibFreq': [ 1735, 1292, 809, 780, 560, 434, 270, 711],
           'NumDeg': [    1,    1,   1,   1,   1,   1,   1,   1]
 },

'NO+': {'hitran': 36,
        'geisa': 45,
        'isotopes': ['46', '56',  '48'],
        'mass':    30.0100,
        'TempExpQR':    1.22450,
        'TempExpGL':   0.500000,
        'VibFreq': [    1876.00],
        'NumDeg': [  1]
 },

'HOBr': {'hitran':37,
         'isotopes': ['169', '161'],
         'mass':    97.0000,
         'TempExpQR':    1.50,
         'TempExpGL':   0.500000,
         'VibFreq': [    3609.00,    1239.00,    724.000],
         'NumDeg': [  1,  1,  1]
 },

'C2H4': {'hitran': 38,
         'geisa': 25,
         'isotopes': ['221', '311'],
         'mass':    28.,
         'TempExpQR':    1.50,
         'TempExpGL':   0.50000,
         'VibFreq': [ 3026, 1625, 1342, 1023, 3103, 1236, 949, 943, 3106, 826, 2989, 1444],
         'NumDeg': [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
 },

'CH3OH': {'hitran': 39,
          'geisa': 44,
          'mass':    32.0000,
          'TempExpQR':    1.50,
          'TempExpGL':   0.500000,
          'VibFreq': [    99999.0],
          'NumDeg': [  0]
 },

'C3H4': {'geisa': 40,
          'mass':    40.0000,
 },

'CH3Br': {'hitran': 40,
          'geisa': 43,
          'isotopes': ['219','211'],
          'mass':    94.,
          'VibFreq': [3026, 1625, 1342, 1023, 3103, 1236, 949, 943, 3106, 826, 2989, 1444],
          'NumDeg': [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
 },

'CH3CN': {'hitran': 41,
          'geisa': 50,
          'isotopes': ['2124'],
          'mass':    41.,
          'VibFreq': [2954, 2267, 1385, 920, 3009, 1448, 1041, 362], },

'CF4': {'hitran': 42,
        'geisa': 49,
        'isotopes': ['29'],
        'mass':    31.,
 },

'C3H8': {'geisa': 28,
         'isotopes': ['221'],
         'mass':    44.,
         'VibFreq': [2977, 2962, 2887, 1476, 1462, 1392, 1158, 869, 369, 2967, 1451, 1278, 940, 216, 2968, 2887, 1464, 1378, 1338, 1054, 922, 2973, 2968, 1472, 1192, 748, 268] },

'C2N2': {'hitran': 48,
         'geisa': 29,
         'isotopes': ['4224'],
         'mass':    52.,
         'VibFreq': [2330, 846, 2158, 503, 234]
 },

'C4H2': {'geisa': 30,
         'hitran': 43,
         'isotopes': ['221'],
         'mass':    50.,
         'VibFreq': [3293, 2184, 874, 3329, 2020, 627, 482, 630, 231] },

'HC3N': {'geisa': 31,
         'hitran': 44,
         'isotopes': ['1224'],
         'mass':    51.,
 },

'HNC':  {'geisa': 46,        # not in Hitran, not terrestrial
         'isotopes': ['142'],
         'mass':    27.,
	 'VibFreq': [2097.0, 713.0, 3311.0],
	 'NumDeg':  [ 1,     2,     1]},

'C6H6': {'geisa': 47,
         'isotopes': ['266'],
         'mass':    78.,
         'VibFreq': [3062, 992, 1326, 673, 3068, 1010, 995, 703, 1310, 1150, 849, 3063, 1486, 1038, 3047, 1596, 1178, 606, 975,	410] },

'C2HD': {'geisa': 48,
         'isotopes': ['122'],
         'mass':    17.,
 },

'BrO':  {
         'isotopes': ['69', '61'],
         'mass':    95.0000,
         'TempExpQR':    1.00,
         'TempExpGL':   0.500000,
         'VibFreq': [    500.0],
         'NumDeg': [  1]
 },

'H2':   {'hitran': 45,
         'isotopes': ['11', '12'],
         'mass':    2.,
         'NumDeg': [  1],
         'VibFreq': [   4160.0]  # data from Smith85 in Rao: Molecular Spectroscopy: Modern Research (1985)
 },

'CS':   {'hitran': 46,
         'isotopes': ['22', '24', '32', '23'],
         'mass':    48.,
 },

'SO3':  {'hitran': 47,
         'geisa': 52,
         'isotopes': ['26'],
         'mass':    80.,
 },

'GeH4':  {'geisa': 26,
         'isotopes': ['411'],
         'mass':    36.,
 },

'COCl2':  {'hitran': 49,
         'isotopes': ['2655', '2657'],
         'mass':    98.,
         'VibFreq': [ 285, 440, 567, 580, 849, 1827]  # data from Pugh&Rao in Rao: Molecular Spectroscopy: Modern Research (1976)
 },

##### added by H. Kawahara ######
'TiO': {
	
	'isotopes': ['48','46','47','49','50'],
	'mass':    64.,
		'TempExpQR':    0.00,
			'TempExpGL':   0.00,
				'VibFreq': [    0.0],
				'NumDeg': [  0]
					},
'46TiO': {
	'isotopes': ['46'],
	'mass':    61.947543,
		'TempExpQR':    0.00,
			'TempExpGL':   0.00,
				'VibFreq': [    0.0],
				'NumDeg': [  0]
					},
'47TiO': {
	
	'isotopes': ['47'],
	'mass':    62.946663,
		'TempExpQR':    0.00,
			'TempExpGL':   0.00,
				'VibFreq': [    0.0],
				'NumDeg': [  0]
					},
'48TiO': {
	'isotopes': ['48'],
	'mass':    63.942857,
		'TempExpQR':    0.00,
			'TempExpGL':   0.00,
				'VibFreq': [    0.0],
				'NumDeg': [  0]
					},
'49TiO': {
	
	'isotopes': ['49'],
	'mass':    64.942780,
		'TempExpQR':    0.00,
			'TempExpGL':   0.00,
				'VibFreq': [    0.0],
				'NumDeg': [  0]
					},
'50TiO': {
	'isotopes': ['50'],
	'mass':    65.939702,
		'TempExpQR':    0.00,
			'TempExpGL':   0.00,
				'VibFreq': [    0.0],
				'NumDeg': [  0]
					},

######### Added by Stevanus K. Nugroho ########
'VO': {
	'isotopes': ['51'],
		'mass':    66.938871,
	'TempExpQR':    0.00,
	'TempExpGL':   0.00,
	'VibFreq': [    0.0],
	'NumDeg': [  0]
		},
'AlO': {
	'isotopes': ['27'],
		'mass':  42.976454,
	'TempExpQR':    0.00,
	'TempExpGL':   0.00,
	'VibFreq': [    0.0],
	'NumDeg': [  0]
		},
'FeH': {
	'isotopes': ['56'],
		'mass':    56.85,
	'TempExpQR':    0.00,
	'TempExpGL':   0.00,
	'VibFreq': [    0.0],
	'NumDeg': [  0]
},
'MgH': {
	'isotopes': ['24'],
		'mass':    24.992867,
	'TempExpQR':    0.00,
	'TempExpGL':   0.00,
	'VibFreq': [    0.0],
	'NumDeg': [  0]
},
	'H_I': { 'isotopes': ['1'], 'kurucz': ['1'], 'mass':  1.00794, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'H_II': { 'isotopes': ['1'], 'kurucz': ['1'], 'mass':  1.00794, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'He_I': { 'isotopes': ['4'], 'kurucz': ['2'], 'mass':  4.002602, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'He_II': { 'isotopes': ['4'], 'kurucz': ['2'], 'mass':  4.002602, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Li_I': { 'isotopes': ['6'], 'kurucz': ['3'], 'mass':  6.941, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Li_II': { 'isotopes': ['6'], 'kurucz': ['3'], 'mass':  6.941, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Be_I': { 'isotopes': ['9'], 'kurucz': ['4'], 'mass':  9.012182, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Be_II': { 'isotopes': ['9'], 'kurucz': ['4'], 'mass':  9.012182, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'B_I': { 'isotopes': ['10'], 'kurucz': ['5'], 'mass':  10.811, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'B_II': { 'isotopes': ['10'], 'kurucz': ['5'], 'mass':  10.811, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'C_I': { 'isotopes': ['12'], 'kurucz': ['6'], 'mass':  12.011, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'C_II': { 'isotopes': ['12'], 'kurucz': ['6'], 'mass':  12.011, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'N_I': { 'isotopes': ['14'], 'kurucz': ['7'], 'mass':  14.00674, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'N_II': { 'isotopes': ['14'], 'kurucz': ['7'], 'mass':  14.00674, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'O_I': { 'isotopes': ['16'], 'kurucz': ['8'], 'mass':  15.9994, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'O_II': { 'isotopes': ['16'], 'kurucz': ['8'], 'mass':  15.9994, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'F_I': { 'isotopes': ['19'], 'kurucz': ['9'], 'mass':  18.9984032, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'F_II': { 'isotopes': ['19'], 'kurucz': ['9'], 'mass':  18.9984032, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ne_I': { 'isotopes': ['20'], 'kurucz': ['10'], 'mass':  20.1797, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ne_II': { 'isotopes': ['20'], 'kurucz': ['10'], 'mass':  20.1797, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Na_I': { 'isotopes': ['23'], 'kurucz': ['11'], 'mass':  22.989768, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Na_II': { 'isotopes': ['23'], 'kurucz': ['11'], 'mass':  22.989768, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Mg_I': { 'isotopes': ['24'], 'kurucz': ['12'], 'mass':  24.305, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Mg_II': { 'isotopes': ['24'], 'kurucz': ['12'], 'mass':  24.305, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Al_I': { 'isotopes': ['27'], 'kurucz': ['13'], 'mass':  26.981539, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Al_II': { 'isotopes': ['27'], 'kurucz': ['13'], 'mass':  26.981539, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Si_I': { 'isotopes': ['28'], 'kurucz': ['14'], 'mass':  28.0855, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Si_II': { 'isotopes': ['28'], 'kurucz': ['14'], 'mass':  28.0855, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'P_I': { 'isotopes': ['31'], 'kurucz': ['15'], 'mass':  30.973762, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'P_II': { 'isotopes': ['31'], 'kurucz': ['15'], 'mass':  30.973762, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'S_I': { 'isotopes': ['32'], 'kurucz': ['16'], 'mass':  32.066, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'S_II': { 'isotopes': ['32'], 'kurucz': ['16'], 'mass':  32.066, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cl_I': { 'isotopes': ['35'], 'kurucz': ['17'], 'mass':  35.4527, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cl_II': { 'isotopes': ['35'], 'kurucz': ['17'], 'mass':  35.4527, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ar_I': { 'isotopes': ['39'], 'kurucz': ['18'], 'mass':  39.948, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ar_II': { 'isotopes': ['39'], 'kurucz': ['18'], 'mass':  39.948, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'K_I': { 'isotopes': ['39'], 'kurucz': ['19'], 'mass':  39.0983, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'K_II': { 'isotopes': ['39'], 'kurucz': ['19'], 'mass':  39.0983, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ca_I': { 'isotopes': ['40'], 'kurucz': ['20'], 'mass':  40.078, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ca_II': { 'isotopes': ['40'], 'kurucz': ['20'], 'mass':  40.078, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sc_I': { 'isotopes': ['45'], 'kurucz': ['21'], 'mass':  44.95591, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sc_II': { 'isotopes': ['45'], 'kurucz': ['21'], 'mass':  44.95591, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ti_I': { 'isotopes': ['47'], 'kurucz': ['22'], 'mass':  47.88, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ti_II': { 'isotopes': ['47'], 'kurucz': ['22'], 'mass':  47.88, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'V_I': { 'isotopes': ['50'], 'kurucz': ['23'], 'mass':  50.9415, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'V_II': { 'isotopes': ['50'], 'kurucz': ['23'], 'mass':  50.9415, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cr_I': { 'isotopes': ['52'], 'kurucz': ['24'], 'mass':  51.9961, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cr_II': { 'isotopes': ['52'], 'kurucz': ['24'], 'mass':  51.9961, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Mn_I': { 'isotopes': ['54'], 'kurucz': ['25'], 'mass':  54.93805, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Mn_II': { 'isotopes': ['54'], 'kurucz': ['25'], 'mass':  54.93805, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Fe_I': { 'isotopes': ['55'], 'kurucz': ['26'], 'mass':  55.847, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Fe_II': { 'isotopes': ['55'], 'kurucz': ['26'], 'mass':  55.847, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Co_I': { 'isotopes': ['58'], 'kurucz': ['27'], 'mass':  58.9332, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Co_II': { 'isotopes': ['58'], 'kurucz': ['27'], 'mass':  58.9332, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ni_I': { 'isotopes': ['58'], 'kurucz': ['28'], 'mass':  58.6934, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ni_II': { 'isotopes': ['58'], 'kurucz': ['28'], 'mass':  58.6934, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cu_I': { 'isotopes': ['63'], 'kurucz': ['29'], 'mass':  63.546, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cu_II': { 'isotopes': ['63'], 'kurucz': ['29'], 'mass':  63.546, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Zn_I': { 'isotopes': ['65'], 'kurucz': ['30'], 'mass':  65.39, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Zn_II': { 'isotopes': ['65'], 'kurucz': ['30'], 'mass':  65.39, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ga_I': { 'isotopes': ['69'], 'kurucz': ['31'], 'mass':  69.723, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ga_II': { 'isotopes': ['69'], 'kurucz': ['31'], 'mass':  69.723, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ge_I': { 'isotopes': ['72'], 'kurucz': ['32'], 'mass':  72.61, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ge_II': { 'isotopes': ['72'], 'kurucz': ['32'], 'mass':  72.61, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'As_I': { 'isotopes': ['74'], 'kurucz': ['33'], 'mass':  74.92159, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'As_II': { 'isotopes': ['74'], 'kurucz': ['33'], 'mass':  74.92159, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Se_I': { 'isotopes': ['79'], 'kurucz': ['34'], 'mass':  78.96, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Se_II': { 'isotopes': ['79'], 'kurucz': ['34'], 'mass':  78.96, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Br_I': { 'isotopes': ['79'], 'kurucz': ['35'], 'mass':  79.904, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Br_II': { 'isotopes': ['79'], 'kurucz': ['35'], 'mass':  79.904, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Kr_I': { 'isotopes': ['83'], 'kurucz': ['36'], 'mass':  83.8, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Kr_II': { 'isotopes': ['83'], 'kurucz': ['36'], 'mass':  83.8, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Rb_I': { 'isotopes': ['85'], 'kurucz': ['37'], 'mass':  85.4678, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Rb_II': { 'isotopes': ['85'], 'kurucz': ['37'], 'mass':  85.4678, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sr_I': { 'isotopes': ['87'], 'kurucz': ['38'], 'mass':  87.62, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sr_II': { 'isotopes': ['87'], 'kurucz': ['38'], 'mass':  87.62, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Y_I': { 'isotopes': ['88'], 'kurucz': ['39'], 'mass':  88.90585, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Y_II': { 'isotopes': ['88'], 'kurucz': ['39'], 'mass':  88.90585, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Zr_I': { 'isotopes': ['91'], 'kurucz': ['40'], 'mass':  91.224, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Zr_II': { 'isotopes': ['91'], 'kurucz': ['40'], 'mass':  91.224, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Nb_I': { 'isotopes': ['92'], 'kurucz': ['41'], 'mass':  92.90638, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Nb_II': { 'isotopes': ['92'], 'kurucz': ['41'], 'mass':  92.90638, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Mo_I': { 'isotopes': ['95'], 'kurucz': ['42'], 'mass':  95.94, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Mo_II': { 'isotopes': ['95'], 'kurucz': ['42'], 'mass':  95.94, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Tc_I': { 'isotopes': ['97'], 'kurucz': ['43'], 'mass':  97.9072, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Tc_II': { 'isotopes': ['97'], 'kurucz': ['43'], 'mass':  97.9072, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ru_I': { 'isotopes': ['101'], 'kurucz': ['44'], 'mass':  101.07, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ru_II': { 'isotopes': ['101'], 'kurucz': ['44'], 'mass':  101.07, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Rh_I': { 'isotopes': ['102'], 'kurucz': ['45'], 'mass':  102.9055, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Rh_II': { 'isotopes': ['102'], 'kurucz': ['45'], 'mass':  102.9055, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pd_I': { 'isotopes': ['106'], 'kurucz': ['46'], 'mass':  106.42, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pd_II': { 'isotopes': ['106'], 'kurucz': ['46'], 'mass':  106.42, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ag_I': { 'isotopes': ['107'], 'kurucz': ['47'], 'mass':  107.8682, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ag_II': { 'isotopes': ['107'], 'kurucz': ['47'], 'mass':  107.8682, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cd_I': { 'isotopes': ['112'], 'kurucz': ['48'], 'mass':  112.411, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cd_II': { 'isotopes': ['112'], 'kurucz': ['48'], 'mass':  112.411, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'In_I': { 'isotopes': ['114'], 'kurucz': ['49'], 'mass':  114.818, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'In_II': { 'isotopes': ['114'], 'kurucz': ['49'], 'mass':  114.818, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sn_I': { 'isotopes': ['118'], 'kurucz': ['50'], 'mass':  118.71, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sn_II': { 'isotopes': ['118'], 'kurucz': ['50'], 'mass':  118.71, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sb_I': { 'isotopes': ['121'], 'kurucz': ['51'], 'mass':  121.757, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sb_II': { 'isotopes': ['121'], 'kurucz': ['51'], 'mass':  121.757, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Te_I': { 'isotopes': ['127'], 'kurucz': ['52'], 'mass':  127.6, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Te_II': { 'isotopes': ['127'], 'kurucz': ['52'], 'mass':  127.6, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'I_I': { 'isotopes': ['126'], 'kurucz': ['53'], 'mass':  126.90447, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'I_II': { 'isotopes': ['126'], 'kurucz': ['53'], 'mass':  126.90447, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Xe_I': { 'isotopes': ['131'], 'kurucz': ['54'], 'mass':  131.29, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Xe_II': { 'isotopes': ['131'], 'kurucz': ['54'], 'mass':  131.29, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cs_I': { 'isotopes': ['132'], 'kurucz': ['55'], 'mass':  132.90543, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Cs_II': { 'isotopes': ['132'], 'kurucz': ['55'], 'mass':  132.90543, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ba_I': { 'isotopes': ['137'], 'kurucz': ['56'], 'mass':  137.327, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ba_II': { 'isotopes': ['137'], 'kurucz': ['56'], 'mass':  137.327, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'La_I': { 'isotopes': ['138'], 'kurucz': ['57'], 'mass':  138.9055, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'La_II': { 'isotopes': ['138'], 'kurucz': ['57'], 'mass':  138.9055, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ce_I': { 'isotopes': ['140'], 'kurucz': ['58'], 'mass':  140.115, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ce_II': { 'isotopes': ['140'], 'kurucz': ['58'], 'mass':  140.115, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pr_I': { 'isotopes': ['140'], 'kurucz': ['59'], 'mass':  140.90765, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pr_II': { 'isotopes': ['140'], 'kurucz': ['59'], 'mass':  140.90765, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Nd_I': { 'isotopes': ['144'], 'kurucz': ['60'], 'mass':  144.24, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Nd_II': { 'isotopes': ['144'], 'kurucz': ['60'], 'mass':  144.24, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pm_I': { 'isotopes': ['144'], 'kurucz': ['61'], 'mass':  144.9127, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pm_II': { 'isotopes': ['144'], 'kurucz': ['61'], 'mass':  144.9127, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sm_I': { 'isotopes': ['150'], 'kurucz': ['62'], 'mass':  150.36, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Sm_II': { 'isotopes': ['150'], 'kurucz': ['62'], 'mass':  150.36, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Eu_I': { 'isotopes': ['152'], 'kurucz': ['63'], 'mass':  151.965, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Eu_II': { 'isotopes': ['152'], 'kurucz': ['63'], 'mass':  151.965, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Gd_I': { 'isotopes': ['157'], 'kurucz': ['64'], 'mass':  157.25, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Gd_II': { 'isotopes': ['157'], 'kurucz': ['64'], 'mass':  157.25, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Tb_I': { 'isotopes': ['158'], 'kurucz': ['65'], 'mass':  158.92534, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Tb_II': { 'isotopes': ['158'], 'kurucz': ['65'], 'mass':  158.92534, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Dy_I': { 'isotopes': ['162'], 'kurucz': ['66'], 'mass':  162.5, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Dy_II': { 'isotopes': ['162'], 'kurucz': ['66'], 'mass':  162.5, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ho_I': { 'isotopes': ['164'], 'kurucz': ['67'], 'mass':  164.93032, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ho_II': { 'isotopes': ['164'], 'kurucz': ['67'], 'mass':  164.93032, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Er_I': { 'isotopes': ['167'], 'kurucz': ['68'], 'mass':  167.26, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Er_II': { 'isotopes': ['167'], 'kurucz': ['68'], 'mass':  167.26, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Tm_I': { 'isotopes': ['168'], 'kurucz': ['69'], 'mass':  168.93421, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Tm_II': { 'isotopes': ['168'], 'kurucz': ['69'], 'mass':  168.93421, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Yb_I': { 'isotopes': ['173'], 'kurucz': ['70'], 'mass':  173.04, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Yb_II': { 'isotopes': ['173'], 'kurucz': ['70'], 'mass':  173.04, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Lu_I': { 'isotopes': ['175'], 'kurucz': ['71'], 'mass':  174.967, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Lu_II': { 'isotopes': ['175'], 'kurucz': ['71'], 'mass':  174.967, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Hf_I': { 'isotopes': ['178'], 'kurucz': ['72'], 'mass':  178.49, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Hf_II': { 'isotopes': ['178'], 'kurucz': ['72'], 'mass':  178.49, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ta_I': { 'isotopes': ['180'], 'kurucz': ['73'], 'mass':  180.9479, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ta_II': { 'isotopes': ['180'], 'kurucz': ['73'], 'mass':  180.9479, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'W_I': { 'isotopes': ['183'], 'kurucz': ['74'], 'mass':  183.84, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'W_II': { 'isotopes': ['183'], 'kurucz': ['74'], 'mass':  183.84, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Re_I': { 'isotopes': ['186'], 'kurucz': ['75'], 'mass':  186.207, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Re_II': { 'isotopes': ['186'], 'kurucz': ['75'], 'mass':  186.207, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Os_I': { 'isotopes': ['190'], 'kurucz': ['76'], 'mass':  190.23, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Os_II': { 'isotopes': ['190'], 'kurucz': ['76'], 'mass':  190.23, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ir_I': { 'isotopes': ['192'], 'kurucz': ['77'], 'mass':  192.22, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Ir_II': { 'isotopes': ['192'], 'kurucz': ['77'], 'mass':  192.22, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pt_I': { 'isotopes': ['195'], 'kurucz': ['78'], 'mass':  195.08, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},
	
	'Pt_II': { 'isotopes': ['195'], 'kurucz': ['78'], 'mass':  195.08, 'TempExpQR':    0.00, 'TempExpGL':   0.00, 'VibFreq': [    0.0], 'NumDeg': [  0]},


}


mainMolecules = ['H2O', 'CO2', 'O3', 'N2O', 'CH4', 'CO', 'O2']


####################################################################################################################################

def get_mol_id_nr (gases, database='hitran'):
	""" Build up a dictionary with molecular numbers (data base specific!) as keys and molecular names as values. """
	mol_id = {}
	for mol,val in list(gases.items()):
		molNr = val.get(database,-1)
		if molNr>0: mol_id[molNr]=mol
	return mol_id


####################################################################################################################################

def isotope_id (Mol, Iso, databasetype='hitran'):
	if databasetype=='hitran':
		if Iso:
			if Iso<10:
				IsoNr=Iso
			else:
				try:
					isotopeNumbers = list(map(int,molecules[Mol]['isotopes']))
					IsoNr = isotopeNumbers.index(Iso)+1
				except KeyError:
					raise  SystemExit ('ERROR: invalid/unknown molecule ' + repr(Mol))
				except ValueError:
					print(Mol, molecules[Mol]['isotopes'])
					raise SystemExit ('ERROR: invalid/unknown isotope ' + repr(Iso))
		else:   IsoNr = 0
	else:
		raise SystemExit ('ERROR --- isotope_id:  not yet done')
	return IsoNr


####################################################################################################################################

def get_molec_data (molecule):
	""" Given a dictionary of dictionaries with molecular data (name and attributes), return dictionary of selected molecule. """
	import numpy as np
	try:
		dct = molecules[molecule]
		for key,value in list(dct.items()):
			# translate all list entries into numpy arrays
			if isinstance(value,(list,tuple)): dct[key] = np.array(value)
		dct['molecule'] = molecule
		return dct
	except KeyError:
		raise SystemExit ('ERROR --- get_molec_data:  Sorry, did not find molecule ' + repr(molecule))


####################################################################################################################################

def name_sort_molecules (gases):
	""" Given a dictionary of dictionaries with molecular data (name and further attributes), sort by molecular name. """
	try: import numpy as np
	except ImportError as msg:  raise SystemExit('import error: ' + str(msg))

	numListH=[]; numListG=[]; nameList=[]
	for mol,dat in list(gases.items()):
		numListH.append(dat.get('hitran',-1)); numListG.append(dat.get('geisa',-1));  nameList.append(mol)
	keyList = np.argsort(np.array(nameList))
	nameList = np.take(nameList,keyList)
	numListH = np.take(numListH,keyList)
	numListG = np.take(numListG,keyList)
	print('\n%10s %6s %6s' % ('', 'hitran', 'geisa'))
	for m,h,g in zip(nameList,numListH,numListG): print('%-10s %6i %6i' % (m, h, g))


####################################################################################################################################

def numeric_sort_molecules (gases, criterion='hitran'):
	""" Given a dictionary of dictionaries with molecular data (name, ID numbers, mass, ...), sort numerically. """
	try: import numpy as np
	except ImportError as msg:  raise SystemExit('import error: ' + str(msg))

	numList=[]; namList=[]
	# from master dictionary extract all dictionaries with relevant entries
	for mol,dat in list(gases.items()):
		if dat.get(criterion):
			numList.append(dat[criterion]);  namList.append(mol)
	# indices for reordering
	keyList = np.argsort(np.array(numList))
	# permute elements
	numList = np.take(numList,keyList)
	namList = np.take(namList,keyList)
	if criterion=='mass':
		for m,n in zip(numList,namList): print('%6.2f  %s' % (m, n))
	else:
		for n,m in zip(numList,namList): print('%3i %s' % (n,m))


####################################################################################################################################

if __name__ == "__main__":
	import sys
	from string import ascii_uppercase as uppercase

	# simple command line parsing should be enough here
	if '-h' in sys.argv or '-help' in sys.argv:
		raise SystemExit (__doc__ + "\n End of molecules help")
	elif '-sh' in sys.argv:
		numeric_sort_molecules (molecules, 'hitran')
	elif '-sg' in sys.argv:
		numeric_sort_molecules (molecules, 'geisa')
	elif '-sm' in sys.argv:
		numeric_sort_molecules (molecules, 'mass')
	elif '-sn' in sys.argv:
		name_sort_molecules (molecules)
	elif len(sys.argv)>1 and sys.argv[1][0] in uppercase:
		for m in sys.argv[1:]:
			if m in molecules:  print(m, '\n', molecules[m], '\n')
			else:               print(repr(m), ' --- unknown molecule!\n')
	else:
		# print a list of all known molecules and its essential attributes
		print('%-8s %5s %6s %6s %5s' % ('molec', 'mass', 'hitran', 'geisa', 'iso'))
		for mol,dat in list(molecules.items()):
			print('%-8s %5.1f %6i %6i %5i' % \
			      (mol, dat['mass'], dat.get('hitran',-1), dat.get('geisa',-1), len(dat.get('isotopes',[]))))
