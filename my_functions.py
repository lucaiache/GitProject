import numpy as np

def Gauss(x, *p0):
    f = 0
    p0 = np.reshape(p0,(3,-1))
    A = p0[0,:]
    mu = p0[1,:]
    sig = p0[2,:]
    for i in range(len(A)):
        f = f + A[i]/(np.sqrt(2*np.pi)*sig[i])*np.exp(-np.power((x - mu[i])/sig[i],2)/2) 
    return f


def GaussPlusBaseline(x, *p0):
    f = 0
    q = p0[-2] #prima prendo i parametri q e m per la baseline lineare
    m = p0[-1]
    p0 = p0[:-2]
    p0 = np.reshape(p0,(3,-1))
    A = p0[0,:] # poi i parametri per le cinque gaussiane
    mu = p0[1,:]
    sig = p0[2,:]
    for i in range(len(A)):
        f = f + A[i]/(np.sqrt(2*np.pi)*sig[i])*np.exp(-np.power((x - mu[i])/sig[i],2)/2) 
    f = f + m*x + q
    return f

