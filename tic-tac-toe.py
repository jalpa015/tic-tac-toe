# Two player Tic Tac Toe game in Python.



# define a function to print the board
def print_board(board):
    print()
    print(' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]) + ' ')
    print('-----------')
    print(' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]) + ' ')
    print('-----------')
    print(' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]) + ' ')
    print()

# define a function to check if a player has won
def check_win(board, player):
    # check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# define a function to check if the board is full
def check_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# define a function to check if a move is valid
def check_valid(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True

# define a function to check if a player wants to play again
def play_again():
    print()
    answer = input('Do you want to play again? (y/n): ')
    if answer == 'y' or answer == 'Y':
        return True
    else:
        print('Thanks for playing!')
        print("Bye!")
        return False

# define a function to clear the board
def clear_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
        
# define a function to get the player's move
def get_move(board, player):
    print()
    print(player + "'s turn")
    row = int(input('Enter row: '))
    col = int(input('Enter column: '))
    print("Entered row and column are: ", row-1, col-1)
    while not check_valid(board, row-1, col-1):
        print('Invalid move')
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
    board[row-1][col-1] = player
    return board

# define main to play the game
def main():
    # define two dimensional array
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    #define players
    players = ['X','O']
    print('Welcome to Tic-Tac-Toe')
    print()
    print('This is the board:')
    print_board(board)
    print('To make a move, enter the row and column numbers when prompted')
    print()
    while True:
        for player in players:
            board = get_move(board, player)
            print_board(board)
            if check_win(board, player):
                print(player + ' wins!')
                if not play_again():
                    return
                else:
                    clear_board(board)
                    print_board(board)
                    break
            if check_full(board):
                print('Draw!')
                if not play_again():
                    return
                else:
                    clear_board(board)
                    print_board(board)
                    break

if __name__ == '__main__':
    main()