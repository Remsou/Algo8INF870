import random as rd

for i in range(6,21):
    with open("instances/instance"+str(i)+".txt", "w") as fichier:
        for i in range(1000000):
            fichier.write(str(rd.randint(1,1000))+" "+str(rd.randint(1,1000))+"\n")