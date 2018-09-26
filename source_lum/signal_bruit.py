import numpy as np

def rapp_signal_bruit(B, A):
    residu = np.dot(np.dot(B,A),S)
    SNR = 10*np.log(np.mean(y**2)/np.mean(residu**2))
    return(SNR)
