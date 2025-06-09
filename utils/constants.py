import tkinter as tk

# Font settings
LARGE_FONT = ("Verdana", 12)

# Global variables for slider values
SLIDERX1 = None  # value determining the boundary of the marked area on the time axis
SLIDERX2 = None  # value determining the boundary of the marked area on the time axis
SLIDERY1 = None  # value determining the boundary of the marked area on the parameter axis
SLIDERY2 = None  # value determining the boundary of the marked area on the parameter axis
HISTOGRAMBINSWIDTH = None  # value determining the width of histogram bins
OVERRUNVALUE = None  # overrun line value

# Available parameters for plotting
AVAILABLE_PARAMETERS = [
    'Psi[°]',
    'Hb[ft]',
    'HLat[°]',
    'HLong[°]',
    'Vp[kn]',
    'Vrz[kn]',
    'Nk_L[%]',
    'Nk_P[%]',
    'Nz[g]',
    'Nx[g]',
    'Ny[g]',
    'Theta[°]',
    'Phi[°]',
    'T4_P[°C]',
    'T4_L[°C]',
    'DSS_P[°]',
    'DSS_L[°]',
    'DSS_MAX_P',
    'DSS_MAX_L',
] 