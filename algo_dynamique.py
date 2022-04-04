import numpy as np

objets = [(4,12),(2,1),(2,2),(1,1),(5,2),(4,3),(8,5),(3,2),(10,4),(4,5),(7,5),(1,2),(9,11),(4,4),(8,7),(1,6),(4,2),(8,6),(5,3)]


def SacADos(objets, poidsSac):
    sol = np.zeros((len(objets),poidsSac))
    for i in range(poidsSac):
        sol[0,i] = 0
    
    for i in range(1,len(objets)):
        for j in range(poidsSac):
            if j >= objets[i][1]:
                sol[i,j] = max(sol[i-1, j], sol[i-1, j-objets[i][1]] + objets[i][0])
            else:
                sol[i,j] = sol[i-1,j]
    return sol


print(SacADos(objets,15))