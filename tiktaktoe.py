EMPTY_CELL = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def check_win(board, player):
    win_conditions = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Columns
        ['1', '5', '9'], ['3', '5', '7']  # Diagonals
    ]

    for condition in win_conditions:
        if all(board[cell] == player for cell in condition):
            return True
    return False

def game():
    the_board = {str(i): EMPTY_CELL for i in range(1, 10)}
    current_player = PLAYER_X
    moves_count = 0

    while moves_count < 9:
        print_board(the_board)
        print(f"It's your turn, {current_player}. Move to which place?")

        move = input()
        if move not in the_board or the_board[move] != EMPTY_CELL:
            print("Invalid move! Try again.")
            continue

        the_board[move] = current_player
        moves_count += 1

        if moves_count >= 5 and check_win(the_board, current_player):
            print_board(the_board)
            print(f"\nGame Over.\n**** {current_player} won. ****")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    if moves_count == 9:
        print("\nGame Over.\nIt's a Tie!!")

if __name__ == "__main__":
    while True:
        game()
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() != "y":
            break
