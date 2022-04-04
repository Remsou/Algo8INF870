import random as rd
with open("instances/instance.txt", "w") as fichier:
    for i in range(1000000):
        fichier.write(str(rd.randint(1,1000000))+" "+str(rd.randint(1,1000000))+"\n")