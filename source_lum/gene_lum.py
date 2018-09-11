import numpy as np
import matplotlib.pyplot as plt
import random as rd

def gene_lum_solo(nb_bits):
    signal = []
    for i in range(nb_bits):
        nb_alea = rd.randint(0,1)
        nb_alea *= rd.randint(70,100)/100.0
        signal.append(nb_alea)
    signal = np.array(signal)
    return(signal)

def gene_lum(nb_bits, nb_voisins):
    l = []
    for i in range(nb_voisins):
        l.append(gene_lum_solo(nb_bits))
    return(l)

# nb_bits = 500
#
# s1 = gene_lum_solo(nb_bits)
# s2 = gene_lum_solo(nb_bits)
# X = range(nb_bits)
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.plot(X, s1)
# plt.subplot(1,2,2)
# plt.plot(X, s2)
# plt.show()
