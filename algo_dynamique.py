import numpy as np
import random as rd
import time


objets = np.loadtxt("instances/instance1.txt")


def SacADos(objets, poidsSac):
    tps1 = time.time()
    sol = np.zeros((len(objets),poidsSac+1))
    for i in range(poidsSac+1):
        sol[0,i] = 0
    
    for i in range(1,len(objets)):
        for j in range(poidsSac+1):
            if j >= objets[i,1]:
                sol[i,j] = max(sol[i-1, j], sol[i-1, j-int(objets[i,1])] + objets[i,0])
                    
            else:
                sol[i,j] = sol[i-1,j]
    tps2 = time.time()

    return sol[len(objets)-1,poidsSac], tps2-tps1

print(SacADos(objets, 1000))
