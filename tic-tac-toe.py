import tkinter

#Grilles 

Boutons = [[0,0,0],
           [0,0,0],
           [0,0,0]
           ]


#Joueurs

Joueur_1 = "X"
Joueur_2 = "O"

#Variable si le joueur a gagne

Arret_de_partie = False

#L'étape du jeu, par exemple premier round c'est joueur 1 qui joue

rounds = 0

#Affichage du gagnant

Valeur_du_gagnant = ""

def Affichage_gagnant():
    if Valeur_du_gagnant == "X":
                print("Le Joueur 1 est vainqueur.")
    elif Valeur_du_gagnant == "O":
                print("Le Joueur 2 est vainqueur.")
                
#Vérification de la grille 

def verification():
    global Arret_de_partie
    global Valeur_du_gagnant
    for x in range(3):
        if Boutons[x][0] == Boutons[x][1] == Boutons[x][2] and Boutons[x][0] != 0 and Boutons[x][1] != 0 and Boutons[x][2] != 0:
            Arret_de_partie = True
            Valeur_du_gagnant = Boutons[x][0]
            Affichage_gagnant()
            break
        elif Boutons[0][x] == Boutons[1][x] == Boutons[2][x] and Boutons[0][x] != 0 and Boutons[1][x] != 0 and Boutons[2][x] != 0:
               Arret_de_partie = True
               Valeur_du_gagnant = Boutons[0][x]
               Affichage_gagnant()
               break
        elif Boutons[0][0] == Boutons[1][1] == Boutons[2][2] and Boutons[0][0] != 0 and Boutons[1][1] != 0 and Boutons[2][2] != 0:
            Arret_de_partie = True
            Valeur_du_gagnant = Boutons[0][0]
            Affichage_gagnant()
            break
        elif Boutons[0][2] == Boutons[1][1] == Boutons[2][0] and Boutons[0][2] != 0 and Boutons[1][1] != 0 and Boutons[2][0] != 0:
              Arret_de_partie = True
              Valeur_du_gagnant = Boutons[0][2]
              Affichage_gagnant
              break
        elif Boutons[0][0] != 0 and Boutons[0][1] != 0 and Boutons[0][2] != 0 and Boutons[1][0] != 0 and Boutons[1][1] != 0 and Boutons[1][2] != 0 and Boutons[2][0] != 0 and Boutons[2][1] != 0 and Boutons[2][2] != 0:
              Arret_de_partie = True
              print("Match nul.")






