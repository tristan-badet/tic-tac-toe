
import random

board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]
             ]
signe = ""
def ia(board, signe):
    global aleatoire

    
    list = [0,1,2,3,4,5,6,7,8]

    for x in range(3): 
        for y in range(3): 
            if board[x][y] == " ":
                board[x][y] = "0"
            elif board[x][y] == " X":
                board[x][y] = "1"
            elif board[x][y] == " O":
                board[x][y] = "2"

    for j in range(3):
        for t in range(3):
            if board[j][t] == "0":
                board[j][t] += signe
            elif board[j][t] == "1":
                continue
            elif board[j][t] == "2":
                continue
    
    if board[0][0] == "1" or board[0][0] == "2":
        list.remove(0)
    if board[0][1] == "1" or board[0][1] == "2":
        list.remove(1)
    if board[0][2] == "1" or board[0][2] == "2":
        list.remove(2)
    if board[1][0] == "1" or board[1][0] == "2":
        list.remove(3)
    if board[1][1] == "1" or board[1][1] == "2":
        list.remove(4)
    if board[1][2] == "1" or board[1][2] == "2":
        list.remove(5)
    if board[2][0] == "1" or board[2][0] == "2":
        list.remove(6)
    if board[2][1] == "1" or board[2][1] == "2":
        list.remove(7)
    if board[2][2] == "1" or board[2][2] == "2":
        list.remove(8)
    
    aleatoire = random.choice(list)

    if aleatoire == 0:
        board[0][0] = "O"
        return board[0][0]
    if aleatoire == 1:
        board[0][1] = "O"
        return board[0][1]
    if aleatoire == 2:
        board[0][2] = "O"
        return board[0][2]
    if aleatoire == 3:
        board[1][0] = "O"
        return board[1][0]
    if aleatoire == 4:
        board[1][1] = "O"
        return board[1][1]
    if aleatoire == 5:
        board[1][2] = "O"
        return board[1][2]
    if aleatoire == 6:
        board[2][0] = "O"
        return board[2][0]
    if aleatoire == 7:
        board[2][1] = "O"
        return board[2][1]
    if aleatoire == 9:
        board[2][2] = "O"
        return board[2][2]
    
    
    

                #faut return la position 
print(board)
ia(board, "x")

    






