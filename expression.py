"expression.py permet d'instancier une classe Expression qui représente une expression mathématique"
import math # Importer le module math
import sympy # Importer sympy pour les symboles mathématiques spéciaux
from random import randint, choice # Importer les fonctions nécessaires du module random


racine = sympy.symbols("√")
signes_expression = ["+", "-", "*", "/", "√"] # Signes pouvant être utilisés dans une expression

nombres_str = [str(n) for n in range(0, 10000)]  # Liste contenant des nombres sous forme de chaîne de caractères entre 0 et 10000

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
    nombre = randint(2, max) # Choisir un nombre entre 2 et le maximum indiqué

    while nombre % 2 > 0 or max % nombre > 0: # Tant que le reste de la division du nombre par 2 est supérieur à zéro ou que le reste de la division du max par le nombre est supérieur à zéro
        nombre = randint(2, max) # Choisir à nouveau un nombre

    return nombre # Renvoyer ce nombre

class Expression():
    def __init__(self, nombres=[2], longueur_min = 3, longueur_max = 30, n_max=2048):
        """Expression mathématique.
        - nombres: liste des nombres appartenant à l'expression
        - longueur_min: longueur minimale de l'expression
        - longueur_max : longueur maximale de l'expression
        - n_max: Nombre maximum pouvant apparaître dans l'expression"""

        
        self.nombre_max = n_max # Nombre maximum pouvant apparaître dans l'expression
        self.longueur = randint(longueur_min, longueur_max) # Longueur de l'expression, comprise entre longueur_min et longueur_max
        self.valeur ="" 
        self.nombres = nombres # Liste des nombres de l'expression
        self.valeur = self.generer() # Valeur de l'expression sous forme de chaîne de caractères
        print(self.valeur)
        """for signe in signes_expression and self.valeur:
            print(self.valeur.split(signe))"""
        
        
        

    def generer(self):
        "Générer l'expression"

        generations = 0  # Nombre de générations réalisées pour l'expression
        generations_max = 10  # Nombre maximum de générations possibles
    
        for i in range(1, self.longueur): # Pour toute la longueur de l'expression
            print(f"Valeur sans espaces: '{self.valeur.strip()}'")
            termes_generes = self.valeur.strip().split(" ") # Termes générés dans l'expressions. Ils sont séparés par des espaces
            print(f"Termes générés : {termes_generes}")
            probabilite_nombre = randint(1, 100) # Probabilité de choisir un nombre en %
            probabilite_signe = randint(1, 100) # Probabilité de choisir un signe en %


            while probabilite_nombre == probabilite_signe: # Tant que les probabilités sont égales
                # Les tirer à nouveau
                probabilite_nombre = randint(1, 100)
                probabilite_signe = randint(1, 100)
        

            if len(termes_generes) > 0: # Si au moins un terme a été généré
                if probabilite_nombre > probabilite_signe and not termes_generes[-1].isdigit():  # Si la probabilité de chosir un nombre est supérieure à celle de choisir un signe et que le terme précédent n'est pas un nombre
                    choix = choisir_nombre(max=2048) # Choisir un nombre au hasard

                else: # Sinon
                    if not termes_generes[-1] in signes_expression:
                        if i < self.longueur - 1: # Si on n'est pas au dernier terme de l'expression
                            choix = choisir_signe() # Choisir un signe    


            else: # Si on doit générer le premier terme
                if probabilite_nombre > probabilite_signe: # Si la probabilité de choisir un nombre est supérieure à celle de choisir un signe
                    choix = choisir_nombre(max=2048) # Choisir un nombre au hasard


                else: # Sinon
                    choix = choisir_signe(exclusions=["*", "/", "+"])   # Choisir un signe au hasard, en excluant les opérateurs *, / et + des possibilités



            for signe in  ["*", "/", "+"]: # Pour chacun des signes *, / et +
                while self.valeur.strip().startswith(signe): # Si l'expression commence par l'un de ces caractères interdits en première position
                    if generations >= generations_max: # Si on a atteint le nombre maximum de générations possibles
                        return self.valeur # Arrêter la fonction pour empêcher les récursions infinies
                    
                    else:
                        self.valeur = self.generer()
                        return self.valeur
                    
                else:
                    break
                
                

            choix = str(choix) # On convertit le choix sous forme de chaîne de caractères pour éviter des problèmes de compatibilité entre les types
            self.valeur += f"{choix} "# Ajouter la valeur du choix (nombre ou signe) à l'expression
            print(f"Valeur expr. : '{self.valeur}', choix : '{choix}'")

        return self.valeur  

    def evaluer(self):
        "Evalue l'expression"
        valeur_evaluable = "" # Valeur de la fonction sous sa forme évaluable
        signes_speciaux = {"√": math.sqrt} # Ce dictionnaire regroupe les signes spéciaux d'une expression et les fonctions correspondantes

        for i, terme in enumerate(self.valeur): # Pour chaque terme de l'expression
            if not terme in signes_speciaux: # Si le terme n'est pas un signe spécial
                valeur_evaluable += terme # Ajouter le terme en dur à l'expression sous forme évaluable

            else: # Si le terme est un signe spécial
                terme_suivant = self.valeur[i+1] # Terme suivant dans l'expression
                if terme_suivant.strip(): # Si le terme suivant peut être transformé en entier
                    terme = signes_speciaux[terme](terme_suivant) # Le terme actuel devient la fonction correspondante au signe spécial à laquelle on donne terme_suivant en paramètre


            #print(f"Expression évaluable : {valeur_evaluable}")


        return eval(valeur_evaluable)            
                







                