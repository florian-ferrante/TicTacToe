import random


# On crée la grille vide
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

# Choix du mode
print("=== TIC TAC TOE ===")
print("1. Joueur vs IA (aléatoire)")
print("2. Joueur vs Joueur")
mode = input("Choisis le mode (1 ou 2) : ")

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
if mode == "1":
    print("Tu es ", player, "le bot est ", bot)
else:
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
    

# Boucle principale du jeu
while not end_game:
    if mode == "1" and current_player == bot:
        # Tour du bot, qui joue de manière aléatoire
        print("C'est au bot de jouer")
        empty_case = [i for i in range(9) if board[i] == "-"]
        pos_bot = random.choice(empty_case)
        board[pos_bot] = bot
        show_board()

    else:
        # Tour du joueur humain (ou des deux joueurs si mode 2)
        print("C'est au joueur", current_player, "de jouer.")
        pos = input("Choisis une case (1 à 9) : ")

        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Choisis une case entre 1 et 9 : ")

        pos = int(pos) - 1
        
        # Si la position est libre, on joue
        if board[pos] == "-":
            board[pos] = current_player
        else:
            print("Cette case est déjà prise !")
            continue

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
    if mode =="1":
        print("Le bot a gagné !")
    else:
        print("Le joueur 2 a gagné !")
else:
    print("Match Nul !")

    
show_board()
