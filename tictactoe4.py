#Choix jouer "X/O"
#Afficher grille
#fin du jeu = false
#True / tour(joueur actuel)
#Verifier fin du jeu
#Joueur suivant
#False / afficher resulat.


#Ma variable de la grille du TicTacToe
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

joueur_actuel= ""
game_end = False
winner = ""



#Fonction qui permet au joueur de choisir un symbole
def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir votre signe : (X) ou (O) :")
    while True:
        joueur_actuel = joueur_actuel.upper()
        if joueur_actuel == "X":
            print("Vous avez choisi X, le joueur 2 aura O")
            break
        elif joueur_actuel == "O":
            print("Vous avez choisi O, le joueur 2 aura X")
            break
        else:
            joueur_actuel = input("Veuillez choisir votre signe : (X) ou (O) :")


#Affichage de mon board/
def show_board():
    print("-------------")
    print("| " + board[0],"|", board[1], "|", board[2], "|              1 | 2 | 3 ")
    print("-------------")
    print("| " + board[3],"|", board[4], "|", board[5], "|              4 | 5 | 6 ")
    print("-------------")
    print("| " + board[6],"|", board[7], "|", board[8], "|              7 | 8 | 9 ")
    print("-------------")

#fonction qui annonce le tour du joueur, et empeche de faire un choix autre que (1,9)
def turn(player):
    print("C'est le tour du joueur:", player)
    pos = input("Veuillez choisir un espace vide sur la grille entre 1 et 9 :")

    valid = False
    while valid == False : 
        
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Veuillez choisir un espace vide sur la grille entre 1 et 9 :")
        pos = int(pos) -1
        if board[pos] == "-":
            valid = True
        else:
            print("Vous ne pouvez pas acceder a cette position!")
    board[pos] = player
    show_board()


#Verifier le gagnant/
def verify_win():
    global game_end
    global winner

#Verifier les lignes/
    if board[0] == board[1] == board[2] and board[0] != "-":
        game_end = True
        winner = board[0]
    elif board[3] == board[4] == board[5] and board[3] != "-":
        game_end = True
        winner = board  [3]
    elif board[6] == board[7] == board[8] and board[8] != "-":
        game_end = True
        winner = board[6]
    
#Verifier les colonnes/
    if board[0] == board[3] == board[6] and board[0] != "-":
        game_end = True
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        game_end = True
        winner = board[1]
    elif board[2] == board[5] == board[8] and board[2] != "-":
        game_end = True
        winner = board[2]

#Verifier les diagonales/
    if board[0] == board[4] == board[8] and board[0] != "-":
        game_end = True
        winner = board[0]
    elif board[2] == board[4] == board[6] and board[2] != "-":
        game_end = True
        winner = board[2]


#Verifier si le match est nul/
def verify_draw():
    global game_end
    
    #S'il n'y a plus de "-" dans la grille, le match est nul/
    if "-" not in board:
        game_end = True

#Faire passer au joueur suivant/
def next_player():
    global joueur_actuel

    if joueur_actuel == "X":
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"

#Fonction qui annonce le gagnant/
def result():
    if winner == "X" or winner == "O":
       print("Le gagnant est :", winner)
    else:
       print("Le match est nul/")
       

#fonction qui execute l'algorythme
def jouer():
    choix_joueur()
    show_board()
    while game_end == False:
        turn(joueur_actuel)
        verify_win()
        verify_draw()
        next_player()
    result()

jouer()