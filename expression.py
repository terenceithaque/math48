"expression.py permet d'instancier une classe Expression qui représente une expression mathématique"
import math # Importer le module math
from random import randint, choice # Importer le module random

signes_expression = ["+", "-", "*", "/", "√"] # Signes pouvant être utilisés dans une expression

# dict_signes est un dictionnaire qui associe des noms de fonctions à des symboles mathématiques
dict_signes = {
    "√":math.sqrt

}
def choisir_signe(exclusions=[]):
    """Choisit un signe au hasard dans la liste
    - exclusions: cette liste peut au besoin être remplie de signes à exclure de la sélection"""

    signe = choice(signes_expression) # Choisir un signe au hasard dans la liste

    while signe in exclusions: # Tant que le signe fait partie de ceux à ignorer pour la sélection
        signe = choice(signes_expression) # On choisit à nouveau un signe au hasard

    return signe # On renvoie le signe choisi    


def choisir_nombre(max=2048):
    """Choisit un nombre au hasard entre 2 et max
    - max: Nombre maximal, un entier."""

    assert type(max).__name__ == "int", "max doit être un nombre entier." # Vérifier si max est un nombre entier, et si ce n'est pas le cas, afficher une erreur dans la console.
    nombre = randint(2, max) # Choisir entre 2 et 4096
    return nombre # Renvoyer ce nombre

class Expression():
    def __init__(self, nombres=[2], longueur_min = 3, longueur_max = 30):
        """Expression mathématique.
        - nombres: liste des nombres appartenant à l'expression
        - longueur_min: longueur minimale de l'expression
        - longueur_max : longueur maximale de l'expression"""

        self.longueur = randint(longueur_min, longueur_max) # Longueur de l'expression, comprise entre longueur_min et longueur_max
        self.valeur ="" 
        self.nombres = nombres # Liste des nombres de l'expression
        self.valeur = self.generer() # Valeur de l'expression sous forme de chaîne de caractères
        print(self.valeur)
        """for signe in signes_expression and self.valeur:
            print(self.valeur.split(signe))"""
        

    def generer(self):
        "Générer l'expression"
        for i in range(self.longueur): # Pour toute la longueur de l'expression
            choix = None # Elément choisi au hasard, en fonction des probabilités tirées
            if i == 0: # Si on est au premier terme de l'expression
                probabilite_nombre = randint(0, 100) # Probabilité qu'un nombre soit choisi en %
                probabilite_signe = randint(0, 100) # Probabilité qu'un signe soit choisi en %
                
                
                while probabilite_nombre == probabilite_signe: # Tant que la probabilité de choisir un nombre est égale à celle de choisir un signe
                    # Tirer de nouvelles probabilités en %
                    probabilite_nombre = randint(0, 100) 
                    probabilite_signe = randint(0, 100)

                print(f"{probabilite_nombre} % de chanches de générer un nombre")
                print(f"{probabilite_signe} % de chances de générer un signe")

                if probabilite_nombre > probabilite_signe: # S'il y a plus de probabilités de choisir un nombre qu'un signe
                    choix = choisir_nombre() # Alors on choisit un nombre

                elif probabilite_signe > probabilite_nombre: # Et dans le cas inverse
                    choix = choisir_signe(exclusions=["+", "*", "/"]) # On choisit un signe, en excluant les symboles +, * et / des possibilités


            else: # Sinon
                probabilite_signe = 0 # Probabilité qu'un signe soit choisi, pour l'instant égale à 0
                probabilite_nombre = randint(0, 100) # Probabilité qu'un nombre soit choisi en %
                if i < self.longueur - 1: # On ne peut choisir un signe que si on est avant le dernier terme de l'expression
                    probabilite_signe = randint(0, 100) # Probabilité qu'un signe soit choisi en %

                while probabilite_nombre == probabilite_signe: # Tant que la probabilité de choisir un nombre est égale à celle de choisir un signe
                    # Tirer de nouvelles probabilités en %
                    probabilite_nombre = randint(0, 100)
                    probabilite_signe = randint(0, 100)

                print(f"{probabilite_nombre} % de chanches de générer un nombre")
                print(f"{probabilite_signe} % de chances de générer un signe")


                if probabilite_nombre > probabilite_signe: # S'il y a plus de probabilités de choisir un nombre qu'un signe
                    choix = choisir_nombre() # Alors on choisit un nombre

                elif probabilite_signe > probabilite_nombre: # Et dans le cas inverse
                    choix = choisir_signe() # Choisir un signe au hasard, sans préciser d'exclusions
                    while choix in self.valeur: # Un même signe ne peut pas apparaître plus d'une fois dans l'expression
                        choix = choisir_signe() # Si c'est le cas, choisir un signe à nouveau


                
            choix = str(choix) # On convertit le choix sous forme de chaîne de caractères pour éviter des problèmes de compatibilité entre les types
            self.valeur +=  choix +  " " # Ajouter la valeur du choix (nombre ou signe) à l'expression
            print(f"Valeur expr. : '{self.valeur}', choix : '{choix}'")

        return self.valeur  

    def evaluer(self):
        "Evalue l'expression"
        pass




                