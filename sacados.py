from dataclasses import dataclass
import csv

@dataclass
class objet:
    valeur: int
    masse: int

@dataclass
class sac:
    capacite: int
    total: int
    resume: []

#On initialise la liste d'objets avec le contenu d'un fichier csv. Les cellules sont au format : [valeur,masse]
def initListe():
    with open('file_sac.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    listobjet = []
    for i in range(1, len(data)):
        listobjet.append(objet(int(data[i][0]),int(data[i][1])))

    #print(listobjet)
    return listobjet

#Fonction pour trier la liste par ordre décroissant de valeur 
def resTriDecroissant(liste):
    E=sorted(liste, key=lambda objet: objet.valeur, reverse=True)
    #print(E)
    return E

#Fonction pour trier la liste par ordre de ratio valeur/masse
def resTriRatio(liste):
    E=sorted(liste, key=lambda objet: objet.valeur/objet.masse, reverse=True)
    #print(E)
    return E

def main():
    liste = initListe()

    #On initialise un sac à dos avec 15kg de capacité, 0 pour dire qu'il est vide et une liste vide
    sacados1 = sac(15,0,[])
    sacados2 = sac(15,0,[])
    liste_current1 = resTriDecroissant(liste)
    liste_current2 = resTriRatio(liste)

    for i in range(0, len(liste_current1)):
        if (liste_current1[i].masse <= sacados1.capacite):
            sacados1.capacite -= liste_current1[i].masse
            sacados1.total += liste_current1[i].valeur
            sacados1.resume.append(liste_current1[i])

        if (liste_current2[i].masse <= sacados2.capacite):
            sacados2.capacite -= liste_current2[i].masse
            sacados2.total += liste_current2[i].valeur
            sacados2.resume.append(liste_current2[i])
    print('-------------')
    print(sacados1)
    print(sacados2)
    print('-------------')

    if (sacados1.total > sacados2.total):
        print('methode tri décroissante plus efficace : total de ' + str(sacados1.total) + '€ (contre ' + str(sacados2.total) + '€ )')
    if (sacados1.total < sacados2.total):
        print('methode tri ratio plus efficace : total de ' + str(sacados2.total) + '€ (contre ' + str(sacados1.total) + '€ )')
    else:
        print('meme resultat de : ' + str(sacados1.total) + '€')

if __name__ == "__main__":
    main()