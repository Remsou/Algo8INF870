import algo_approché
import algo_dynamique
import numpy as np
import matplotlib.pyplot as plt


def res():
    for i in range(1,21):
        objets = np.loadtxt("instances/instance"+str(i)+".txt")
        z1, t1 = algo_approché.SacADos(objets, 100)
        z2, t2 = algo_dynamique.SacADos(objets, 100)

        t1 = round(t1, 5)
        t2 = round(t2, 5)
        d = round(((z2 - z1)/z2)*100,5)

        with open("resultats.txt", "a") as fichier:
            fichier.write(str(t1)+" "+str(t2)+" "+str(z1)+" "+str(z2)+" "+str(d)+"\n")


def plot():
    res = np.loadtxt("resultats.txt")
    print(res[:,0])
    x = range(1,21)
    fig, axs = plt.subplots(3)
    axs[0].plot(x, res[:,0], "b", label="approchée")
    axs[0].plot(x, res[:,1], "r", label="exacte")
    axs[0].set_title("Temps d'exécution (en secondes)")
    axs[0].legend(loc="upper left")

    axs[1].plot(x, res[:,2], "b", label="approchée")
    axs[1].plot(x, res[:,3], "r", label="exacte")
    axs[1].set_title("Valeur de la fonction objective")
    axs[1].legend(loc="upper left")

    axs[2].plot(x, res[:,4], "b")
    axs[2].set_title("Ecart relatif de la fonction objective (en %)")

    
    fig.tight_layout()
    plt.show()

def stat():
    res = np.loadtxt("resultats.txt")
    moyenne = np.mean(res,0)
    print(moyenne)



stat()