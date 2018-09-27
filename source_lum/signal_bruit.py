import numpy as np

def rapp_signal_bruit(B, A, S, y):
    residu = np.dot(np.dot(B,A),S) # Le S ici est en réalité S avec une des sources éteintes
    SNR = 10*np.log10(np.mean(np.dot(y,np.transpose(y))/np.mean(np.dot(residu,np.transpose(residu)))))
    return(SNR)
