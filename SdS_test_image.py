import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import gene_image as gi
import gradient as gr
import correl_coef_composante_nb as cc
import recons_images_test_nb as ri

print('je genere puis concatene les images en vecteur .....')

s1, s2, nb_lign, nb_col, image_source1, image_source2 = gi.gene_image()
s1 = s1 - np.mean(s1) # espérance nulle
s2 = s2 - np.mean(s2)

##std signifie écart type (ou norme de vecteurs aléatoites)
s1 = s1/np.std(s1) # on ramène s1 et s2 à une norme de valeur 1
s2 = s2/np.std(s2)
x1_R = s1
x2_R = s2
A11 = 0.6 # coefficients de mélange
A12 = 0.4
A21 = 0.4
A22 = 0.6

x1 = A11 * s1 + A12 * s2
x2 = A21 * s1 + A22 * s2

print('je reconstruis les images de melanges......')
xx1 = (x1 - np.min(x1)) / (np.max(x1) - np.min(x1)) * 255
xx2 = (x2 - np.min(x2)) / (np.max(x2) - np.min(x2)) * 255

image_mel1, image_mel2 = ri.recons_images_test_nb(xx1, xx2, nb_lign, nb_col)

plt.figure(1)
io.imshow(image_source1)
plt.title('sep1')
plt.show()
plt.close()

## Je sais pas quoi faire avec ces trucs là
#colormap
#gray

plt.figure(2)
io.imshow(image_source2)
plt.title('sep2')
#colormap
#gray
plt.show()

plt.figure(3)
io.imshow(image_mel1)
plt.title('mel1')
#colormap
#gray
plt.show()

plt.figure(4)
io.imshow(image_mel2)
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

lambda0 = 1. # hyperparametre : parametre de pénalisation : je cherche des sources ayant un ecart constant, ici = 1
# j'ai du l'appeler lambda0 car lambda est une fonction python

y1=x1 # Je demarre avec mes sources melangees/observees
y2=x2

indice = 1 # compteur d'affichage



for i in range(1,nb_iter):
    DJ = gr.compute_gradient(B,y1,y2,x1,x2,lambda0)

    B=B-mu*DJ # mise a jour de la matrice de separation

    y1=B[0,0]*x1+B[0,1]*x2 # mise a jour d'une estimation des sources separees (approximation des sources avant melange)
    y2=B[1,1]*x2+B[1,0]*x1

    y1 = y1-np.mean(y1)
    y2 = y2-np.mean(y2)

    plt.close() #Affichage
    if(i==indice*100): # on affiche les images qui se "démélangent" toutes les 100 itérations et on recalcule la corrélation
        indice += indice
        print('je reconstruis les images separees......')
        yy1=(y1-np.min(y1))/(np.max(y1)-np.min(y1))*255
        yy2=(y2-np.min(y2))/(np.max(y2)-np.min(y2))*255
        image_sep1, image_sep2 = ri.recons_images_test_nb(yy1,yy2,nb_lign,nb_col)
        plt.figure(5)
        io.imshow(image_sep1)
        plt.title('sep1')
        #colormap
        #gray

        plt.figure(6)
        io.imshow(image_sep2)
        plt.title('sep2')
        #colormap
        #gray
        plt.show() # remplace le drawnow (normalement)

        Mat_or_cor_source = cc.correl_coef_composante_nb(s1,s2) # Calcul de la correlation entre les sources avant melange
        plt.pause(1)

        Mat_mel_cor = cc.correl_coef_composante_nb(x1,x2) # Calcul de la correlation entre les sources melangees

        Mat_sep_cor = cc.correl_coef_composante_nb(y1,y2) # Calcul de la correlation entre les sources separees
        plt.pause(5)
