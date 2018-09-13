import numpy as np

L = 0.5
H = 1

def coefs(D):
    " on veut les coefs tels que x1 = a1*s1 + a3*s2, x2 = a2*s1 + a3*s2"
    A11 = 1/(H**2)
    A21 = 1/(H**2)
    A12 = 1/(1+(L+D)**2)
    A22 = 1/(H**2 + L**2)

    A11norm = A11/(A11+A12)
    A21norm = A21/(A21+A22)
    A12norm = A12/(A12+A11)
    A22norm = A22/(A22+A21)

    return(A11norm, A21norm, A12norm, A22norm)
