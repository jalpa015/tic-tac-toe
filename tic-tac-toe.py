# define two dimensional array
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#define players
players = ['X','O']

# define a function to print the board
def print_board(board):
    print()
    print(' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]) + ' ')
    print('-----------')
    print(' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]) + ' ')
    print('-----------')
    print(' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]) + ' ')
    print()

print('Welcome to Tic-Tac-Toe!')
print('Player 1 is X and Player 2 is O')
print_board(board)

# define boolean variable to check if game is over
game_over = False
player_index = 0
while not game_over:
    player = players[player_index]
    print('Player ' + player + '\'s turn')
    print('Enter the row and column number of the box you want to mark')
    row = int(input('Row: ')) - 1
    col = int(input('Column: ')) - 1
    board[row][col] = player
    print_board(board)

    # check if player has won player wins if there are three Xs or Os in a row, column or diagonal
    
    if board[0][0] == board[0][1] == board[0][2] == player or \
        board[1][0] == board[1][1] == board[1][2] == player or \
        board[2][0] == board[2][1] == board[2][2] == player or \
        board[0][0] == board[1][0] == board[2][0] == player or \
        board[0][1] == board[1][1] == board[2][1] == player or \
        board[0][2] == board[1][2] == board[2][2] == player or \
        board[0][0] == board[1][1] == board[2][2] == player or \
        board[0][2] == board[1][1] == board[2][0] == player:
        print('Player ' + player + ' wins!')
        game_over = True
        break

    # # check if game is a tie
    # if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
    #     print('Game is a tie!')
    #     game_over = True
    #     break

    if game_over:
        print('Game Over!')
        break
    else:
        # switch players
        if player_index == 0:
            player_index = 1    
        else:
            player_index = 0

    # # ask if players want to play again
    # play_again = input('Do you want to play again? (y/n): ')
    # if play_again == 'y':
    #     board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    #     print_board(board)
    # else:
    #     break
