import numpy as np

def rapp_signal_bruit(B, A, s2, y):
    residu = np.dot(B,A)[0][1]*s2 # Le S ici est en réalité S avec une des sources éteintes
    SNR = 10*np.log10(np.mean(y*y)/np.mean(residu*residu))
    return(SNR)
