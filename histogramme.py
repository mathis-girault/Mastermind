import random
import matplotlib.pyplot as plt
import numpy as np
import io
import sys

import codebreaker0
import codemaker0
from play import play


def recup_print(play, codemaker, codebreaker):
    """ Fonction qui permet de récuperer du texte qui a été écrit dans la console 
    python par une fonction donnée en argument"""
    # rediriger stdout dans un buffer :
    sys.stdout = io.StringIO()
    # appel de la fonction qui remplira stdout (donc le buffer)
    play(codemaker,codebreaker)
    # récupérer le contenu du buffer :
    s = sys.stdout.getvalue()    
    # fermer le buffer :
    sys.stdout.close()    
    # rediriger stdout vers la sortie standart :
    sys.stdout = sys.__stdout__
    # Maintenant on récupère la partie de l'affichage qui nous intéresse :
    s = s[-15:]
    nombre = ''
    for e in s:
        if e.isdigit():
            nombre += str(e)
    return int(nombre)


def histogram(n):
    """ Fonction qui trace un histogramme répertoriant le nombre d'essais nécessaires
    pour que codemaker0 arrive à réussir, sur n parties"""
    # On créé la liste du nombre d'essais pour les n parties : 
    list = []
    for i in range(n):
        list.append(recup_print(play, codemaker0, codebreaker0))
    # On trace l'histogramme :
    plt.hist(list, range = (0,8000), bins = 800)
    plt.title("Nombres d'essais") 
    plt.show()


def trace_histo2(n): # methode exacte
    p = len(common.COLORS)**common.LENGTH
    list2 = np.random.geometric(1/p, n)
    plt.hist(list2, range = (0,8000), bins = 8000, color='yellow')
    plt.title("Nombres d'essais") 
    plt.show()