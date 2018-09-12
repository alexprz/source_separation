import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import gene_lum as gl
import gradient as gr
import correl_coef_composante_nb as cc

print('je genere puis concatene les images en vecteur .....')

nb_bits = 500
X = range(500)

[s1, s2] = gl.gene_lum(nb_bits, 2)
source1, source2 = s1[:], s2[:]
s1 = s1 - np.mean(s1) # espérance nulle
s2 = s2 - np.mean(s2)

##std signifie écart type (ou norme de vecteurs aléatoites)
s1 = s1/np.std(s1) # on ramène s1 et s2 à une norme de valeur 1
s2 = s2/np.std(s2)
x1_R = s1
x2_R = s2
A11 = 0.10 # coefficients de mélange
A12 = 0.90
A21 = 0.20
A22 = 0.80

x1 = A11 * s1 + A12 * s2
x2 = A21 * s1 + A22 * s2

print('je reconstruis les signaux de melanges......')
xx1 = (x1 - np.min(x1)) / (np.max(x1) - np.min(x1))
xx2 = (x2 - np.min(x2)) / (np.max(x2) - np.min(x2))

plt.figure(1)
plt.plot(X, source1)
plt.title('source1')
plt.show()

## Je sais pas quoi faire avec ces trucs là
#colormap
#gray

plt.figure(2)
plt.plot(X, source2)
plt.title('source2')
#colormap
#gray
plt.show()

plt.figure(3)
plt.plot(X, xx1)
plt.title('mel1')
#colormap
#gray
plt.show()

plt.figure(4)
plt.plot(X, xx2)
plt.title('mel2')
##colormap
##gray
plt.show()

x1 = x1 - np.mean(x1) # espérance nulle
x2 = x2 - np.mean(x2)

x1 = x1 / np.std(x1) # norme de valeur 1
x2 = x2 / np.std(x2)

print('l algo tourne.......')

nb_iter = 500

B = np.eye(2) # Initialisation de la matrice de separation

mu=0.01 #pas dans la descente du gradient

lambda0 = 0. # hyperparametre : parametre de pénalisation : je cherche des sources ayant un ecart constant, ici = 1
# j'ai du l'appeler lambda0 car lambda est une fonction python

y1=x1 # Je demarre avec mes sources melangees/observees
y2=x2

indice = 1 # compteur d'affichage

std1 = np.std(y1)
std2 = np.std(y2)

for i in range(nb_iter+1):
    DJ = gr.compute_gradient(B,y1,y2,x1,x2,lambda0)

    B=B-mu*DJ # mise a jour de la matrice de separation
    B[0,0] /= std1
    B[0,1] /= std1

    B[1,0] /= std2
    B[1,1] /= std2


    y1=B[0,0]*x1+B[0,1]*x2 # mise a jour d'une estimation des sources separees (approximation des sources avant melange)
    y2=B[1,1]*x2+B[1,0]*x1

    std1 = np.std(y1)
    std2 = np.std(y2)
    y1 = y1/std1
    y2 = y2/std2

    y1 = y1-np.mean(y1)
    y2 = y2-np.mean(y2)

    plt.close() #Affichage
    if(i==indice*100): # on affiche les images qui se "démélangent" toutes les 100 itérations et on recalcule la corrélation
        indice += 1
        print('je reconstruis les signaux separes......')
        yy1=(y1-np.min(y1))/(np.max(y1)-np.min(y1))
        yy2=(y2-np.min(y2))/(np.max(y2)-np.min(y2))
        print(np.std(y1))
        print(np.std(y2))
        plt.figure(5)
        plt.plot(X,yy1)
        plt.title('sep1')
        #colormap
        #gray

        plt.figure(6)
        plt.plot(X,yy2)
        plt.title('sep2')
        #colormap
        #gray
        plt.show() # remplace le drawnow (normalement)

        Mat_or_cor_source = cc.correl_coef_composante_nb(s1,s2) # Calcul de la correlation entre les sources avant melange
        print(Mat_or_cor_source)

        Mat_mel_cor = cc.correl_coef_composante_nb(x1,x2) # Calcul de la correlation entre les sources melangees

        Mat_sep_cor = cc.correl_coef_composante_nb(y1,y2) # Calcul de la correlation entre les sources separees
        # Afficher matrice corr à chaque étape
        print(Mat_sep_cor)

plt.figure(1)
plt.subplot(1,2,1)
plt.plot(X, yy1, 'r')
plt.plot(X, source1, 'b')
# plt.title('Comparaison des signaux séparés et originaux 1')
plt.subplot(1,2,2)
plt.plot(X, yy2, 'r')
plt.plot(X, source2, 'b')
# plt.title('Comparaison des signaux séparés et originaux 1')
plt.show()
