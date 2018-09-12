import numpy as np

L = 0.5
H = 1

def coefs(D):
    " on veut les coefs tels que x1 = a1*s1 + a3*s2, x2 = a2*s1 + a3*s2"
    a1 = 1/(H**2)
    a2 = 1/(H**2)
    a3 = 1/(H**2 + L**2)
    a4 = 1/(1+(L+D)**2)

    a1norm = a1/(a1+a4)
    a2norm = a2/(a2+a3)
    a3norm = a3/(a3+a2)
    a4norm = a4/(a4+a1)

    return(a1norm, a2norm, a3norm, a4norm)

    
