import numpy as np

def recons_images_test_nb(y1_R,y2_R,nb_lign,nb_col):
    return([np.uint8(np.reshape(y1_R, (nb_lign, nb_col))),np.uint8(np.reshape(y2_R, (nb_lign, nb_col)))])
