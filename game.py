game = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_game(game):
    print(
        f"{game[0]} {game[1]} {game[2]} \n{game[3]} {game[4]} {game[5]} \n{game[6]} {game[7]} {game[8]}")


def play(player):
    command = input(f"{player}'s turn where do you want to play? ")
    text = ["top-left", "top", "top-right", "left", "center",
            "right", "bottom-left", "bottom", "bottom-right"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if command == text[i]:
            command = numbers[i]
    valid_command = "123456789"
    if str(command) not in valid_command:
        print("invalid command. Try again.")
        play(player)
        return 0
    if not space_taken(game, int(command) - 1):
        game[int(command) - 1] = player
    else:
        print("space taken. Try again.")
        play(player)
        return 0


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


def space_taken(game, position):
    if game[position] == "X" or game[position] == "O":
        return True
    else:
        return False


def is_tie(game):
    numbers = "123456789"
    for i in game:
        if str(i) in numbers:
            return False
    return True


while True:
    if is_tie(game) == True:
        print("Tie.")
        exit()
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
