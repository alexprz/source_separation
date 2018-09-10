import numpy as np
##from skimage import pydoc_data
from skimage import io
from skimage import color
from path import *

def gene_image():

    ###noir et blanc
    barbara_image = io.imread(pathBarbara)
    nb_lig, nb_col  = barbara_image.shape
    N = nb_col*nb_lig
    Grey = barbara_image
    Grey = np.reshape(Grey, (N, 1))
    Grey1 = Grey/255
    Grey1 = np.array([(g-np.min(Grey1))/(np.max(Grey1)-np.min(Grey1)) for g in Grey1])
    Grey1 = np.reshape(Grey1, (nb_lig,nb_col))

    ###couleur
    lena_image = io.imread(pathLena)
    lena_image_grey = color.rgb2grey(lena_image)
    R, G, B = np.reshape(lena_image[:,:,0], (N,1)), np.reshape(lena_image[:,:,1], (N,1)), np.reshape(lena_image[:,:,2], (N,1))
    R, G, B = R/255, G/255, B/255
    Grey2 = np.reshape(lena_image_grey, (N,1))/255
    Grey2 = np.array([(g-np.min(Grey2))/(np.max(Grey2)-np.min(Grey2)) for g in Grey2])
    Grey2 = np.reshape(Grey2, (nb_lig,nb_col))
    return(Grey1, Grey2, nb_lig, nb_col, barbara_image, lena_image_grey)
