"Script principal du jeu"
import math # Importer le module math de Python
from random import randint # Importer la fonction randint du module random

# Grille du jeu
grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]] 

# dict_signes est un dictionnaire qui associe des noms de fonctions à des symboles mathématiques
dict_signes = {
    "√": math.sqrt,
    "|x|": abs,

}


def tirer_nombre():
    "Tire un nombre au hasard, 2 ou 4"
    probabilite4 = randint(0, 100) # Probabilité qu'un 4 soit tiré, en %
    print(f"{probabilite4} % de chances qu'un 4 soit tiré.")
    if probabilite4 >= 67: # Si cette probabilité est supérieure ou égale à 67 %
        return 4 # Tirer un 4

    else: # Si les chances sont inférieures à 67 %
        return 2 # Tirer un 2



def generer_expression(nombres=[2]):
    """Générer une expression mathématique avec un ou plusieurs nombre
       - nombres: liste des nombres appartenant à l'expression"""

    pass   

print(tirer_nombre())        



