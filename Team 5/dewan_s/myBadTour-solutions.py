"""
Dewan Sunnah

There are techincally 4 errors (1 type of error occurs multiple times) in this program

the knights tour has solutions for board sizes above 5+
once you get to board size 8 it can take really long to get the solution to print

so focus on sizes 5 - 7 inclusive
"""

def can_move(board, board_size, row, col):
    if row < board_size and row >= 0 and col < board_size and col >= 0 and board[row][col] == 0:
        return True
    return False

def solve(board, board_size, row, col, counter):
    print(f"{counter}: [{row}][{col}]")
    if not can_move(board, board_size, row, col):
        return False
    
    board[row][col] = counter
    if counter == (board_size*board_size):
        return True

    next_row = row + 2
    next_col = col + 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    next_row = row + 2
    next_col = col - 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    next_row = row - 2
    next_col = col + 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    next_row = row - 2
    next_col = col - 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    next_row = row + 1
    next_col = col + 2
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0    

    next_row = row + 1
    next_col = col - 2 
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    next_row = row - 1
    next_col = col + 2
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    next_row = row - 1
    next_col = col - 2
    if solve(board, board_size, next_row, next_col, counter + 1):
        board[row][col] = counter
        return True
    board[row][col] = 0

    return False

def make_board(board_size):
    new_board = []
    for n in range(0,board_size):
        new_row = []
        for n in range(0,board_size):
            new_row.append(0)
        new_board.append(new_row)
    return new_board

def print_board(board):
    for i in range(0,len(board)):
        print(board[i])

b_size = input("Input the size of the board: ")
b_size = int(b_size)
chess_board = make_board(b_size)
solve(chess_board, b_size, 0, 0, 1)
print_board(chess_board)
