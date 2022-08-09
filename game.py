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
    else:
        print("Command invalid. Try again")
        play(player)


def does_player_win(game, player):
    win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9),
           (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]
    for i in range(8):
        count_symbol = 0
        for x in range(3):
            if game[win[i-1][x-1]-1] == player:
                count_symbol += 1
                if count_symbol == 3:
                    return True
    return False


while True:
    play("X")
    print_game(game)
    if does_player_win(game, "X"):
        print("X won!")
        exit()
    play("O")
    print_game(game)
    if does_player_win(game, "O"):
        print("O won!")
        exit()
