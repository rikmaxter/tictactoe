# Tic-Tac-Toe

Tic-Tac-Toe interactif codé avec [`tkinter`](https://docs.python.org/3/library/tkinter.html). Voir `notes.md` pour la structure de l'UI.

## Description

- Choix du symbole `X` ou `O`.
- Jeu contre l'ordinateur qui place ses pions aléatoirement.
- Bouton `Play again` pour rejouer directement.
- Taille de grille adaptable.

Le jeu est codé dans la classe `TicTacToe`, on peut créer une instance comme suit :

```python
game = TicTacToe(n=3)   # 3x3 grid
game.run()              # lancer le jeu
```

## Installation

1. Cloner le repo :
    ```
    git clone git@github.com:rikmaxter/tictactoe.git
    cd repo_name
    ```
2. Installer `tkinter` :
    - **Ubuntu/Debian** : `sudo apt install python3-tk`
    - **Arch Linux** : `sudo pacman -S tk`

3. Lancer le jeu :
    ```
    python main.py
    ``` 

## Tests

Des tests ont été réalisés avec [`unittest`](https://docs.python.org/3/library/unittest.html) et couvrent les cas suivants :

- Victoire sur les lignes, colonnes ou (anti-)diagonales
- Comptage des tours 
- Détection d'une grille pleine (égalité)
- Placement d'un pion sur la grille

``` 
python tests.py
``` 