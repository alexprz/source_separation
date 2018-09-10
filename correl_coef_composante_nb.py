import numpy as np

def correl_coef_composante_nb(im1_R,im2_R):
    N = len(im1_R)
    moy_1R = np.mean(im1_R)
    moy_2R = np.mean(im2_R)

<<<<<<< HEAD
    Mat_cor_R = np.zeros(2)
    Mat_cor_G = np.zeros(2) # Ces deux lignes sont
    Mat_cor_B = np.zeros(2) # inutiles en noir et blanc, on utilise que 'R'
=======
    Mat_cor_R = np.zeros((2,2))
    Mat_cor_G = np.zeros((2,2))
    Mat_cor_B = np.zeros((2,2))
    # Mat_cor_G = np.zeros(2) # Ces deux lignes sont
    # Mat_cor_B = np.zeros(2) # inutiles en noir et blanc, on utilise que 'R'
>>>>>>> 647d448ab53b8f843aadc1fd7c0102ff148b86f7

    ec_1R = np.std(im1_R)
    ec_2R = np.std(im2_R)

    ec_R = np.transpose(np.array([ec_1R,ec_2R]))

    moy_R = np.transpose(np.array([moy_1R,moy_2R]))

    ima_R = np.array([im1_R[:],im2_R[:]])

    print(ima_R.shape)


    for i in range(2):
        for j in range(2):
            prod_term = [(ima_R[i,k] - moy_R[i])*(ima_R[j,k] - moy_R[j]) for k in range(N)] # cette partie remplace le produit terme à terme de Matlab
            Mat_cor_R[i,j] = (1/(N*ec_R[i]*ec_R[j]))*np.sum(prod_term)

    return(Mat_cor_R)
