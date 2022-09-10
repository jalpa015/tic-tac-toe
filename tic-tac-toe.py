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


print_board(board)
