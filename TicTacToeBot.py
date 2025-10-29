import random

# On crée la grille vide
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

# Le joueur choisit son symbole
player = input("Choisis ton signe (X ou O) : ")
#Si le joueur demande autre chose que X ou O, on redemande de faire un choix.
while player not in ["X", "O"]:
    player = input("Choisis entre X ou O : ")

# Attribution de l'autre symbole au bot
if player == "X":
    bot = "O"
else:
    bot = "X"

# On annonce le choix du symbole, ainsi que le fait que X commence toujours, que ça soit le bot, ou le joueur
print("Tu es ", player, "le bot est ", bot)
print("X commence toujours.")

# Le joueur actuel
current_player = "X"

# Variable pour savoir si le jeu est fini
end_game = False
winner = None

# Fonction pour afficher la grille
def show_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|   1 2 3")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|   4 5 6")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|   7 8 9")
    print("-------------")

# On affiche la grille au début
show_board()

# Boucle principale du jeu
# Tant que le jeu n'est pas terminé, le joueur ou le bot continue de jouer
while not end_game:
    if current_player == player:
        # Tour du joueur humain
        print("C'est ton tour :", player)
        pos = input("Choisis une case (1 à 9) : ")
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Choisis une case entre 1 et 9 : ")
        # Rajouter un -1 a l'entier demandé par le joueur, pour tenir compte de l'indexation
        pos = int(pos) - 1
        #Si la position demandé est "-" donc libre, on utilise le choix du joueur
        if board[pos] == "-":
            board[pos] = player
        #Sinon, on annonce que la case est prise, et demande une nouvelle fois de faire un choix
        else:
            print("Cette case est déjà prise, essaie encore.")
            continue
    else:
        # Tour du bot, import random qui joue de manière aléatoire
        print("C'est au bot de jouer")
        empty_case = [i for i in range(9) if board[i] == "-"]
        pos_bot = random.choice(empty_case)
        board[pos_bot] = bot

    show_board()

    # Vérifie les combinaisons gagnantes
    #Verifier les lignes/
    if board[0] == board[1] == board[2] and board[0] != "-":
        end_game = True
        winner = board[0]
    elif board[3] == board[4] == board[5] and board[3] != "-":
        end_game = True
        winner = board  [3]
    elif board[6] == board[7] == board[8] and board[8] != "-":
        end_game = True
        winner = board[6]
    
    #Verifier les colonnes/
    if board[0] == board[3] == board[6] and board[0] != "-":
        end_game = True
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        end_game = True
        winner = board[1]
    elif board[2] == board[5] == board[8] and board[2] != "-":
        end_game = True
        winner = board[2]

    #Verifier les diagonales/
    if board[0] == board[4] == board[8] and board[0] != "-":
        end_game = True
        winner = board[0]
    elif board[2] == board[4] == board[6] and board[2] != "-":
        end_game = True
        winner = board[2]

    # Vérifie s’il y a égalité
    # S'il n'y a plus de "-" et qu'il n'y a pas de gagnant, alors c'est un match nul
        if "-" not in board and winner is None:
            end_game = True

    # Change de joueur si le jeu n’est pas fini
    if not end_game:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Fin du jeu
if winner == player:
    print("Tu as gagné !")
elif winner == bot:
    print("Le bot a gagné !")
else:
    print("Match nul !")
