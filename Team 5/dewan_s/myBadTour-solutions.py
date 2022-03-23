"""
Originally implemented and given with implicit errors by Dewan Sunnah
Reviewed and debugged by Henry Baum

myBadTour is recreational math problem that solves the touring knight problem using
a brute-force recursive method.

The Touring Knight problem is a mathematical problem that aims to complete a knight's
tour of a chessboard. This is done when a knight chess piece starts on a tile, then moves
to new, unvisited one, and continues moving, until every tile has been visited at most once.

The program prompts the user to create a squared tile board by the requested size, then
finds a solution for the tour. By using the brute force/recursive method, the program works
by trying the first possible legal move the knight can make, and continues to make another move,
until it's stuck with no legal moves. It then backtracks, and continues moving, cycling between
backtracking and moves until a solution is found.

Limitations:
Since this method is extremely computationally expensive, a solution can only be realistically
found on modern personal computer with a board size no higher than 7 x 7. In fact, trying to
find the solution on an 8 x 8 standard chess board can take approximately 4*10^51 possible moves!
Because of this, the user promp will double check if the user wishes to run the script (and
likely need to force quit) for any board size beyond 7.
"""

def can_move(board, board_size, row, col):
    """
    --- Helper Function to determine if knight can move to tile ---
    Does a bounds check to make sure row and col are within the bounds the board,
    as well as check to see if tile is unvisited, denoted by the cell value equaling
    to zero

        Parameters:
            board : [[int]] - 2D list of ints, each cell represents a value:
                0 : knight has yet to visit tile
                1 <= x <= board_size^2 : which numbered move the knight landed on that tile
            board_size : int - the size of the squared board (width and height bounds)
            row : int - the attempted row location on the board
            col : int - the attempted coloumn location on the board
        Returns:
            If the row is in bounds of the board size,
            and if the col is in bounds of the board size,
            and the tile has yet to be visited (equals zero),
            then returns boolean True.
            Otherwise, returns False.
    """
    if row < board_size and row >= 0 and col < board_size and col >= 0 and board[row][col] == 0:
        return True
    return False

def solve(board, board_size, row, col, counter):
    """
    --- Solving the Knight's Tour ---
    This function solves the knight's your by using brute-force recursion, moving the piece forward
    anytime it can make a legal move, until it can, then backtracks, triying a different move, and
    continues the cycle until the knight moves into the final tile (board_size * board_size), signifying
    a possible solution has been found. 

    The function will cycle through the board 2D list, modifying the board 2D list as it tests for solutions

    Note: It is possible for there to be no solutions if board size is 2, 3, or 4. In such cases, the board
    will be entirely zeros.

        Parameters:
            board : [[int]] - 2D list of ints, each cell represents a value:
                0 : knight has yet to visit tile
                1 <= x <= board_size^2 : which numbered move the knight landed on that tile
            board_size : int - the size of the squared board (width and height bounds)
            row : int - the attempted row location on the board
            col : int - the attempted coloumn location on the board
            counter : int - signifies which numbered move the knight is on
        Returns:
            None, though will modify board that contains the path solution for the knight's tour
    """
    # First checks if location is a legal move
    if not can_move(board, board_size, row, col):
        # Backtrack to attempt a different maneuver
        return False
    
    # Else, move is legal, and sets tile number to counter
    board[row][col] = counter

    # If the counter is the final tile, then the solution has been found
    # This will return true for all calling functions in the recursive tree
    if counter == (board_size*board_size):
        return True

    # Else, the knight must move to different tiles
    # There are 8 possible moves the knight can make
    # The function attempts them in a sequential order and continues to
    # do so, calling solve() each time till the final move is found
    # If it is, then they return true for the previous recursive function

    # Maneuver #1
    next_row = row + 2
    next_col = col + 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True

    # Maneuver #2
    next_row = row + 2
    next_col = col - 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True

    # Maneuver #3
    next_row = row - 2
    next_col = col + 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True

    # Maneuver #4
    next_row = row - 2
    next_col = col - 1
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True

    # Maneuver #5
    next_row = row + 1
    next_col = col + 2
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True
    
    # Maneuver #6
    next_row = row + 1
    next_col = col - 2 
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True

    # Maneuver #7
    next_row = row - 1
    next_col = col + 2
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True

    # Maneuver #8
    next_row = row - 1
    next_col = col - 2
    if solve(board, board_size, next_row, next_col, counter + 1):
        return True
    
    # If all possible moves has been exhausted with no solutions,
    # then the knight must backtrack.
    # Mark the space as unused and return False to for calling
    # function to attempt next maneuver
    board[row][col] = 0
    return False

def make_board(board_size):
    """
    --- Helper function to create blank board ---
    Creates a squared board based on user input board size
        Parameters:
            board_size : int - a positive number
        Returns:
            new_board : [[int]] - a 2D list that's board_size by board_size,
                                  each cell with the value 0
    """
    new_board = []
    for n in range(0,board_size):
        new_row = []
        for n in range(0,board_size):
            new_row.append(0)
        new_board.append(new_row)
    return new_board

def print_board(board):
    """
    --- Helper function to print board ---
    Loops through list to print every cell contents
    In this case, every cell is a list with an int
        Parameters:
            board : []
        Return:
            None - print contents directly to console/terminal
    """
    for i in range(0,len(board)):
        print(board[i])

def main():
    """
    --- Main driver for script for user input --
    Prompts user for board size, then creates a board with make_board(),
    begins solution with solve(), then calls print_board() to print results.
    By default, it starts the knight's position in the most upper-left tile.
    Note: Will double-check with user for printing board sizes beyond 7.
        Parameters:
            None
        Returns:
            None
    """

    # Input validation loop to check if user is SURE they want a board size beyond 7.
    confirmed = False
    while not confirmed:
        b_size = input("Input the size of the board: ")
        b_size = int(b_size)
        if b_size >= 8:
            confirm_prompt = input(f"Are you sure you want a board size {b_size}? You will most likely have to force quit. Press 'y' to confirm.")
            if confirm_prompt[:1].lower() == 'y':
                confirmed = True
        else:
            confirmed = True

    chess_board = make_board(b_size)
    solve(chess_board, b_size, 0, 0, 1)
    print_board(chess_board)

main()
