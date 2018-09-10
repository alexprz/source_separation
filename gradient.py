import numpy as np

def compute_gradient(B,y1,y2,x1,x2,lam1):

    ##moyennes de vecteurs multipliés termes à termes
    m_y1 = np.mean(y1)
    m_y1_2 = np.mean(y1*y1)
    m_y1_3 = np.mean(y1*y1*y1)
    m_y1_4 = np.mean(y1*y1*y1*y1)
    m_y1_5 = np.mean(y1*y1*y1*y1*y1)
    m_y1_6 = np.mean(y1*y1*y1*y1*y1*y1)

    m_y2 = np.mean(y2)
    m_y2_2 = np.mean(y2*y2)
    m_y2_3 = np.mean(y2*y2*y2)
    m_y2_4 = np.mean(y2*y2*y2*y2)
    m_y2_5 = np.mean(y2*y2*y2*y2*y2)
    m_y2_6 = np.mean(y2*y2*y2*y2*y2*y2)

    K1 = np.array([1, m_y1, m_y1_2, m_y1_3])
    K2 = np.array([1, m_y2, m_y2_2, m_y2_3])

    M1 = np.array([[1, m_y1, m_y1_2, m_y1_3],
    [m_y1, m_y1_2, m_y1_3, m_y1_4], [m_y1_2, m_y1_3, m_y1_4, m_y1_5],
    [m_y1_3, m_y1_4, m_y1_5, m_y1_6]])

    M2 = np.array([[1, m_y2, m_y2_2, m_y2_3],
    [m_y2, m_y2_2, m_y2_3, m_y2_4], [m_y2_2, m_y2_3, m_y2_4, m_y2_5],
    [m_y2_3, m_y2_4, m_y2_5, m_y2_6]])


    P1 = np.array([0,1,2 * m_y1,3*(m_y1_2)])
    P2 = np.array([0,1,2 * m_y2,3 * (m_y2_2)])
    w1 = np.dot(np.np.linalg.inv(M1), P1)
    w2 = np.dot(np.np.linalg.inv(M2), P2)

    Psi_y1 = w1[0] + w1[1] * y1 + w1[2] * y1*y1 + w1[3] * y1*y1*y1
    Psi_y2 = w2[0] + w2[1] * y2 + w2[2] * y2*y2 + w2[3] * y2*y2*y2
    Psi_y = [Psi_y1, Psi_y2]

    M_Psi11 = np.mean(Psi_y1 * x1)
    M_Psi12 = np.mean(Psi_y1 * x2)
    M_Psi21 = np.mean(Psi_y2 * x1)
    M_Psi22 = np.mean(Psi_y2 * x2)

    y1 = y1 - np.mean(y1)
    y2 = y2 - np.mean(y2)

    temp1 = 4 * (np.mean(y1*y1) - 1) * y1
    temp2 = 4 * (np.mean(y2*y2) - 1) * y2
    m_y1_x1 = np.mean(temp1 * x1)
    m_y1_x2 = np.mean(temp1 * x2)
    m_y2_x1 = np.mean(temp2 * x1)
    m_y2_x2 = np.mean(temp2 * x2)
    pen = np.array([[m_y1_x1, m_y1_x2], [m_y2_x1, m_y2_x2]])
    return(np.dot(np.array([[M_Psi11, M_Psi12],[M_Psi21, M_Psi22]]),np.transpose(B))-np.eye(2) + np.dot(np.dot(lam1,pen),np.transpose(B)))

