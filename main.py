"Script principal du jeu"
import math # Importer le module math de Python
from random import randint # Importer la fonction randint du module random
from expression import *  # Importer le fichier local expression.py pour pouvoir créer des expressions mathématiques

directions = ["haut", "bas", "gauche", "droite"] # Liste des directions dans lesquelles le joueur peut déplacer les tuiles

# Grille du jeu
grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]] 



def est_puissance_de(n=4, puiss=2):
    """Renvoie un booléen en vérifiant si un nombre n est une puissance de puiss
    n: Nombre dont on vérifie s'il est puissance
    puiss: Puissance à comparer avec n
    La formule utilisée est n % puiss == 0"""

    assert puiss != 0, "La puissance doit être strictement positive ou négative: impossible de diviser par 0."

    if n % puiss == 0: # Si le reste de n divisé par pow est égal à 0, alors n est une puissance de puiss
        return True

    return False    










def grille_pleine():
    "Vérifier si la grille de jeu est pleine"
    lignes_pleines = 0 # Nombre de lignes pleines (sans cases dont le contenu vaut 0)
    for ligne in grille:
        if not 0 in ligne: # Si il n'y a aucune case libre (dont le contenu vaut 0) dans la ligne
            lignes_pleines += 1 # Augmenter le nombre de lignes pleines de 1

    return lignes_pleines == len(grille) # On vérifie si le nombre de lignes pleines correspond au nombre de lignes dans la grille, auquel cas on renvoie True, sinon False       



def tirer_nombre():
    "Tire un nombre au hasard, 2 ou 4"
    probabilite4 = randint(0, 100) # Probabilité qu'un 4 soit tiré, en %
    print(f"{probabilite4} % de chances qu'un 4 soit tiré.")
    if probabilite4 >= 67: # Si cette probabilité est supérieure ou égale à 67 %
        return 4 # Tirer un 4

    else: # Si les chances sont inférieures à 67 %
        return 2 # Tirer un 2



expression = Expression(longueur_min=3, longueur_max=7, n_max=2048)
print(expression.valeur)

print(expression.evaluer())

#print(est_puissance_de(4, 2))
#print(help(est_puissance_de))

"""
if grille_pleine():
    print(f"La grille {grille} est pleine")

else:
    print(f"La grille {grille} n'est pas pleine.")    
"""


