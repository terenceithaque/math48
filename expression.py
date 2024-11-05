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
        signe = choice(signes_expression) # On choisit à nouveau un signe au hasardsym

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

        self.symboles_valeurs = {
            "x" : choisir_nombre(max=16),
            "y" : choisir_nombre(max=16),
            "z": choisir_nombre(max=16)
        } # Dictionnaire référençant chaque symbole et leur valeur numérique choisie au hasard

        print(f"Symboles & valeurs correspondantes : {self.symboles_valeurs}")

        self.nombre_max = n_max # Nombre maximum pouvant apparaître dans l'expression
        self.longueur = randint(longueur_min, longueur_max) # Longueur de l'expression, comprise entre longueur_min et longueur_max
        self.valeur ="" 
        self.nombres = nombres # Liste des nombres de l'expression
        self.valeur = self.generer(renvoie_sympified=False) # Valeur de l'expression sous forme exploitable par le programme
        print(self.valeur)
        """for signe in signes_expression and self.valeur:
            print(self.valeur.split(signe))"""
        
        
        

    def generer(self, renvoie_sympified=True):
        """Générer l'expression
        renvoie_sympified: si égal à True, alors l'expression est renvoyée sous forme directement exploitable, sinon elle est renvoyée sous forme de chaîne de caractères."""

        self.x, self.y, self.z = sympy.symbols("x y z") # Créer des symboles x, y et z
        
        print(type(self.x), type(self.y), type(self.z))
        formes = [(2*self.x)**2 + (3*self.x) -1, (5*self.x)**3 - (2*self.x)**2 + self.x -1, self.x**4 + (2*self.y)**3 - (3*self.z)**2 + self.x + 1] # Modèles d'expressions polynômes

        forme_expr = choice(formes)  # Choisir une forme d'expression aléatoire

        print(f"Forme choisie : {forme_expr}")
        print(forme_expr.args)

        expression = "" #  Expression finale sous forme de chaîne de caractères
        for terme in forme_expr.args: # Pour chaque terme de la forme d'expression choisie
            terme_str = str(terme) # Convertir le terme sous forme de chaîne de caractères
            expression += terme_str # ajouter le terme à  l'expression
            
        

            
        for symbole, valeur in self.symboles_valeurs.items(): # Pour chaque symbole tel que x, y ou z et leur valeur associée
            if symbole in expression: # Si le symbole est présent dans l'expression
                expression = expression.replace(symbole, str(valeur)) # Le remplacer par la valeur numérique correspondante

        
        if renvoie_sympified: # Si on doit renvoyer l'expression sous forme exploitable par sympy / Python
            self.valeur = expression
            return sympy.sympify(self.valeur)
        
        else : # Sinon
            self.valeur = expression
            return self.valeur # Renvoyer l'expression sous forme de chaîne de caractères

    def evaluer(self):
        "Evalue l'expression"
        print(f"{self.valeur} : {type(self.valeur)}")
        return sympy.sympify(self.valeur).evalf()
                







                