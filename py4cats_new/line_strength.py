#!/usr/bin/python
import sys
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
from astropy import constants as const
from astropy import units as u
from scipy import interpolate


def linestrength_normal(gf,nui,hatnu,QT,T):
    #line strength in the unit of cm2/s/species. see Sharps & Burrows equation(1)
    #all quantities should be converted to the cgs unit
    #gf   : g(statistical weight) * f(oscillator strength)
    #nui  : initial wavenumber in cm-1
    #hatnu: line position in cm-1
    #QT: partition function 
    #T   : temperature 

    eesu=const.e.esu
    ee=(eesu*eesu).to(u.g*u.cm*u.cm*u.cm/u.s/u.s).value
    me=const.m_e.cgs.value
    c=const.c.cgs.value
    h=const.h.cgs.value
    k=const.k_B.cgs.value
    
    fac0=np.pi*ee/me/c
    fac1=-h*c*nui/k/T
    fac2=-h*c*hatnu/k/T
    Snorm=fac0*gf*np.exp(fac1)/QT*(-np.expm1(fac2))

    #np.expm1(x) = exp(x) -1 
    
    return Snorm

def linestrength_hitran_zero(gf,nui,hatnu,QT0,T0):
    #line strength used in HITRAN form (cm/species). see Sharps & Burrows equation(11)
    #QT0=Q(T=296 K)
	#print "REFERENCE TEMPERATURE=",T0
    c=const.c.cgs.value
    Snorm=linestrength_normal(gf,nui,hatnu,QT0,T0)
    Sh0=np.array(Snorm/c)

    #cleanup
    mask=(Sh0<0.0)
    Sh0[mask]=0.0

    return Sh0

def Sh0toSh(Sh0,nui,hatnu,QT,T,QT0,T0):
#line strength at T0 to line strength at T in HITRAN form
    c=const.c.cgs.value
    h=const.h.cgs.value
    k=const.k_B.cgs.value    
    w=-h*c/k
    fac1T=w*nui/T
    fac1T0=w*nui/T0
    fac2T=w*hatnu/T
    fac2T0=w*hatnu/T0

    Sh=Sh0*np.exp(fac1T)/np.exp(fac1T0)*QT0/QT*np.expm1(fac2T)/np.expm1(fac2T0)

    return Sh

