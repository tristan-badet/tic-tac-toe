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
          
#Vérification de la grille 

def verification_X():
    global Arret_de_partie
    global Bouton_1,Bouton_2, Bouton_3, Bouton_4, Bouton_5,Bouton_6,Bouton_7,Bouton_8,Bouton_9
    if Bouton_1["text"] == Bouton_2["text"] == Bouton_3["text"] == " X":
          Arret_de_partie = True
          messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")    
    elif Bouton_4["text"] == Bouton_5["text"] == Bouton_6["text"] == " X":
          Arret_de_partie = True
          messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")
    elif Bouton_7["text"] == Bouton_8["text"] == Bouton_9["text"] == " X":
          Arret_de_partie = True
          messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")
    elif Bouton_1["text"] == Bouton_4["text"] == Bouton_7["text"] == " X":
          Arret_de_partie = True
          messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")
    elif Bouton_2["text"] == Bouton_5["text"] == Bouton_8["text"] == " X":
          Arret_de_partie = True
          messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")
    elif Bouton_3["text"] == Bouton_6["text"] == Bouton_9["text"] == " X":
          Arret_de_partie = True
          messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")
    elif Bouton_1["text"] == Bouton_5["text"] == Bouton_9["text"] == " X":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")   
    elif Bouton_3["text"] == Bouton_5["text"] == Bouton_7["text"] == " X":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 1 a gagné")
    elif rounds == 10:
            messagebox.showinfo("Tic-Tac-Toe", "Match nul entre les deux joueurs")

def verification_O():
      global Arret_de_partie
      global Bouton_1,Bouton_2, Bouton_3, Bouton_4, Bouton_5,Bouton_6,Bouton_7,Bouton_8,Bouton_9
      if Bouton_1["text"] == Bouton_2["text"] == Bouton_3["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")    
      elif Bouton_4["text"] == Bouton_5["text"] == Bouton_6["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")
      elif Bouton_7["text"] == Bouton_8["text"] == Bouton_9["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")
      elif Bouton_1["text"] == Bouton_4["text"] == Bouton_7["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")
      elif Bouton_2["text"] == Bouton_5["text"] == Bouton_8["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")
      elif Bouton_3["text"] == Bouton_6["text"] == Bouton_9["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")
      elif Bouton_1["text"] == Bouton_5["text"] == Bouton_9["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")   
      elif Bouton_3["text"] == Bouton_5["text"] == Bouton_7["text"] == " O":
            Arret_de_partie = True
            messagebox.showinfo("Tic-Tac-Toe", "Le joueur 2 a gagné")
      elif rounds == 10:
            messagebox.showinfo("Tic-Tac-Toe", "Match nul entre les deux joueurs")

    
        
def placement_de_signe(y):
    global rounds
    if rounds%2 != 0 and Arret_de_partie == False and y["text"] == " ":
        y["text"] += "X"
        rounds += 1
        verification_X()
    elif rounds%2 == 0 and Arret_de_partie == False and y ["text"] == " ":
        y["text"] += "O"
        rounds += 1 
        verification_O()
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