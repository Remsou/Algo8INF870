import numpy as np
import time

objets = np.loadtxt("instances/instance.txt")

def SacADos(objets,poidsSac):
    tps1 = time.time()
    tab = []
    sol = 0
    poidsSol = 0
    for i in range(len(objets)):
        tab.append((objets[i][0]/objets[i][1], objets[i][0], objets[i][1]))
    
    tab.sort()
    tab.reverse()
    
    for i in range(len(objets)):
        if poidsSol+tab[i][2] < poidsSac:
            sol += tab[i][1]
            poidsSol+=tab[i][2]
    tps2 = time.time()
    return sol, tps2-tps1

print(SacADos(objets,30))