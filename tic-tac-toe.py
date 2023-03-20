import tkinter
from tkinter import messagebox

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

rounds = 1

#Affichage du gagnant

Valeur_du_gagnant = ""

def Affichage_gagnant():
    if Valeur_du_gagnant == "X":
                messagebox.showinfo("Tic-Tac-Toe", "Le Joueur 1 a gagné.")
    elif Valeur_du_gagnant == "O":
                messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné.")
                
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
              messagebox.showinfo("Tic-Tac-Toe", "C'est un match nul entre le joueur 1 et le joueur 2.")

def placement_de_signe(y):
    global rounds
    if rounds%2 != 0 and Arret_de_partie == False and y["text"] == " ":
        y["text"] += "X"
        rounds += 1
        #A voir avec tkinter voir video widget
    elif rounds%2 == 0 and Arret_de_partie == False and y ["text"] == " ":
        y["text"] += "O"
        rounds += 1 
    else:
        messagebox.showerror("Tic-Tac-Toe", "La case est déjà utilisée")

# Début de l'interface graphique

tic_tac_toe = tkinter.Tk()
tic_tac_toe.title("Tic-Tac-Toe")

#Boutons du morpion

Bouton_1 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_1))
Bouton_1.grid(row=0, column=0)

Bouton_2 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_2))
Bouton_2.grid(row=0, column=1)

Bouton_3 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_3))
Bouton_3.grid(row=0, column=2)

Bouton_4 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_4))
Bouton_4.grid(row=1, column=0)

Bouton_5 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_5))
Bouton_5.grid(row=1, column=1)

Bouton_6 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_6))
Bouton_6.grid(row=1, column=2)

Bouton_7 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_7))
Bouton_7.grid(row=2, column=0)

Bouton_8 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_8))
Bouton_8.grid(row=2, column=1)

Bouton_9 = tkinter.Button(tic_tac_toe, text=" ", height=5, width=10, command=lambda: placement_de_signe(Bouton_9))
Bouton_9.grid(row=2, column=2)

tic_tac_toe.mainloop()