
# Code by Roselyn, rosa-com on GitHub

def game():

    def print_board(board):
        print(f"[{str(board[6])}] | [{str(board[7])}] | [{str(board[8])}]")
        print('----+----+----')
        print(f"[{str(board[3])}] | [{str(board[4])}] | [{str(board[5])}]")
        print('----+----+----')
        print(f"[{str(board[0])}] | [{str(board[1])}] | [{str(board[2])}]")

    def check_win(board):
        if board[0] == board[1] == board[2]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[3] == board[4] == board[5]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[6] == board[7] == board[8]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[0] == board[3] == board[6]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[1] == board[4] == board[7]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[2] == board[5] == board[8]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[0] == board[4] == board[8]:
            print(f"{current_player['name']} is the winner!")
            exit()
        elif board[6] == board[4] == board[2]:
            print(f"{current_player['name']} is the winner!")
            exit()

    board = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]

    continue_game = True

    count = 0

    player1 = {
        "name": "",
        "symbol": "o"}

    player2 = {
        "name": "",
        "symbol": "x"}

    player1["name"] = input("What is Player 1 called: ")
    player2["name"] = input("What is Player 2 called: ")

    while continue_game:

        print(f"It is {player1['name']}'s turn")
        print_board(board)
        space = input("What space do you choose?")
        space = int(space)

        # This needs to be done separate from the 2nd while loop or else there will be an index error
        while 0>space or space>10:
            print("That is not a valid space, please try again")
            space = input("What space do you choose?")
            space = int(space)

        # Logic for if the space is already filled
        while space is not board[space-1]:
            print("That is not a valid space, please try again")
            space = input("What space do you choose?")
            space = int(space)
        board[space-1] = player1["symbol"]
        current_player = player1

        check_win(board)
        count += 1

        # this is the only point where a draw can happen since the count is an odd number.
        if count == 9:
            print("\nGame Over.\n")
            print(f"It's a tie between {player1['name']} and {player2['name']}")
            exit()

        print(f"It is {player2['name']}'s turn")
        print_board(board)
        space = input("What space do you choose?")
        space = int(space)

        while 0 > space or space > 10:
            print("That is not a valid space, please try again")
            space = input("What space do you choose?")
            space = int(space)

        while space is not board[space - 1]:
            print("That is not a valid space, please try again")
            space = input("What space do you choose?")
            space = int(space)
        board[space - 1] = player2["symbol"]
        current_player = player2

        check_win(board)
        count += 1

    print(f"It was a draw between {player1['name']} and {player2['name']}")
    exit()

print("Simple Tic Tac Toe game.\n"
      "Would you like to play?\n")

if input("Enter Y or N ") == "Y":
    game()
else:
    exit
