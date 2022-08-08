game_finished = False
game = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_game(game):
    print(
        f"{game[0]} {game[1]} {game[2]} \n{game[3]} {game[4]} {game[5]} \n{game[6]} {game[7]} {game[8]}")


def play(player):
    command = input("Where do you want to play? ")
    if player == "X":
        if command == "top-left":
            game[0] = "X"
        elif command == "top":
            game[1] = "X"
        elif command == "top-right":
            game[2] = "X"
        elif command == "left":
            game[3] = "X"
        elif command == "center":
            game[4] = "X"
        elif command == "right":
            game[5] = "X"
        elif command == "bottom-left":
            game[6] = "X"
        elif command == "bottom":
            game[7] = "X"
        elif command == "bottom-right":
            game[8] = "X"
    elif player == "O":
        if command == "top-left":
            game[0] = "O"
        elif command == "top":
            game[1] = "O"
        elif command == "top-right":
            game[2] = "O"
        elif command == "left":
            game[3] = "O"
        elif command == "center":
            game[4] = "O"
        elif command == "right":
            game[5] = "O"
        elif command == "bottom-left":
            game[6] = "O"
        elif command == "bottom":
            game[7] = "O"
        elif command == "bottom-right":
            game[8] = "O"


while game_finished == False:
    play("X")
    print_game(game)
    play("O")
    print_game(game)
