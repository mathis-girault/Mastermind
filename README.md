# Mastermind - EN version below

## Introduction
C'est un projet de deuxième année de prépa visant à construire un mastermind fonctionnel, et notamment à développer des versions efficaces du codemaker et du codebreaker.
Dans un premier temps nous avons juste coder des fonctions qui marchent, puis dans un deuxième temps il nous fallait aller plus loins. pour cela, on a implémenté une version du codemaker qui peut tricher, de manière subtile et invisible. D'autre part, on a implémenté une version du codebreaker qui avait pour objectif d'être le plus optimisée possible, dans le pire des cas.

Le fonctionnement général est assez simple : **codemaker** choisit une solution, et à tour de rôles, **codebreaker** va envoyer un essai. **Codemaker** va en retour renvoyer une évaluation de cet essai selon les règles du jeu mastermind.
On continue jusqu'à que **codebreaker** ai réussi à trouver la solution.

## Utilisation

Pour jouer, il suffit de lancer le programme ***play.py***. Vous pouvez changer les versions de codemakers et codebreakers utilisés (voir ci-dessous).

## Liste des fichiers

- play.py : programme central du jeu, qui vient faire jouer une version de codemaker contre une version de codebreaker. Possibilité aussi de faire jouer l'humain contre soit codemaker soit codebreaker. Un sous programme à l'intérieur permet de faire jouer deux versions de codemaker et codebreaker mais en enregistrant les logs d'une partie dans un fichier texte 
- Les codebreakers 
    - codebreaker0.py : première version qui teste au hasard
    - codebreaker1.py : deuxième version qui teste une combinaison parmis celles non testées
    - codebreaker2.py : troisième version, qui prend en compte l'évaluation de codemaker pour tester une combinaison possible au vu des évaluations précedentes
    - codebreaker3.py : dernière version, qui est optimisée pour chercher le meilleur essai possible *version fonctionnelle mais très lente*
- Les codemakers
    - codemaker0.py : première version non fonctionnelle car ne renvoie pas une évaluation correcte
    - codemaker1.py : deuxième version, fonctionelle qui renvoie simplement l'évaluation associée à l'essai de codebreaker
    - codemaker2.py : dernière version qui est capable de triche ; cette version cherche à choisir une solution qui renvoie le moins d'informations possibles
- common.py : fichier qui comprend diverses fonction utiles à codemaker et à codebreaker. Contient : *choices*, *evaluation*, *creer_possibles*, *donner_possibles*, *maj_possibles* et *nombres_possibles*
- histogramme.py : fichier qui répertorie différentes fonctions de tracés pour évaluer les performances des différentes versions de **codemaker** et **codebreaker**
- logs : dossier où se trouve les parties enregistrées par la deuxième version de la fonction play dans *play.py*
- check_codemaker.py : programme qui vérifie, pour une partie enregistrée dans *logs* si le codemaker a triché de manière visible
- annexe.py : fichier où se situent une deuxième version de la fonction *evaluation* de common.py, et une autre version de codemaker3.py, avec une tentative d'utilisation de programation dynamique. Ce sont deux programmes stockés pour une potentielle future amélioration.
- tests.py : fichier qui comprends quelques tests associés aux fonctions de common.py

---

# Mastermind

## Introduction
This is a second year project to build a functional mastermind, and in particular to develop efficient versions of the codemaker and the codebreaker.
At first we just coded functions that would work, then in a second time we had to go further. For that, we implemented a version of codemaker that can cheat, in a subtle and invisible way. On the other hand, we implemented a version of the codebreaker which had for objective to be the most optimized possible, in the worst case.

The general operation is quite simple: **codemaker** chooses a solution, and in turn, **codebreaker** will send a test. In return, **codemaker** will send back an evaluation of this trial according to the rules of the mastermind game.
We continue until **codebreaker** has found the solution.

## Usage

To play, you just have to launch the program ***play.py***. You can change the versions of codemakers and codebreakers used (see below).

## List of files

- play.py : central program of the game, which makes play a version of codemaker against a version of codebreaker. It is also possible to play the human against either codemaker or codebreaker. A sub-program inside allows to play two versions of codemaker and codebreaker but recording the logs of a game in a text file 
- The codebreakers 
    - codebreaker0.py : first version that tests randomly
    - codebreaker1.py : second version which tests a combination among those not tested
    - codebreaker2.py : third version, which takes into account the evaluation of codemaker to test a possible combination according to the previous evaluations
    - codebreaker3.py : last version, which is optimized to look for the best possible test *functional but very slow version*.
- The codemakers
    - codemaker0.py : first version not functional because it doesn't return a correct evaluation
    - codemaker1.py : second version, functional which simply returns the evaluation associated to the codebreaker test
    - codemaker2.py : last version which is capable of cheating ; this version tries to choose a solution which returns the least possible information
- common.py: file that includes various functions useful to codemaker and codebreaker. Contains : *choices*, *evaluation*, *creer_possibles*, *donner_possibles*, *maj_possibles* and *nombres_possibles*.
- histogram.py: file that lists different plot functions to evaluate the performance of different versions of **codemaker** and **codebreaker**.
- logs : folder where are the games recorded by the second version of the play function in *play.py*.
- check_codemaker.py : program that checks, for a game recorded in *logs*, if the codemaker has cheated in a visible way
- appendix.py : file where a second version of the *evaluation* function of common.py is located, and another version of codemaker3.py, with an attempt to use dynamic programming. These are two programs stored for potential future improvement.
- tests.py : file that includes some tests associated with the functions of common.py
