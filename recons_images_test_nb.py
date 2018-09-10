import numpy as np

def recons_images_test_nb(y1_R,y2_R,nb_lign,nb_col):
    
    for j in range(0, nb_lign):
        image_R1[j,:] = y1_R[nb_col*j + 1 : nb_col*(j+1)]
        image_R2[j,:] = y2_R[nb_col*j + 1 : nb_col*(j+1)]
    
    image_reconst1[:,:]=image_R1
    image_reconst2[:,:]=image_R
    return([np.uint8(image_reconst1),np.uint8(image_reconst2)])
 
 
 
