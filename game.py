game_finished = False
game = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_game(game):
    print(
        f"{game[0]} {game[1]} {game[2]} \n{game[3]} {game[4]} {game[5]} \n{game[6]} {game[7]} {game[8]}")


def play(player):
    command = input(f"{player}'s turn where do you want to play? ")
    if command == "top-left":
        game[0] = player
    elif command == "top":
        game[1] = player
    elif command == "top-right":
        game[2] = player
    elif command == "left":
        game[3] = player
    elif command == "center":
        game[4] = player
    elif command == "right":
        game[5] = player
    elif command == "bottom-left":
        game[6] = player
    elif command == "bottom":
        game[7] = player
    elif command == "bottom-right":
        game[8] = player


while game_finished == False:
    play("X")
    print_game(game)
    play("O")
    print_game(game)
