"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # Looping through to count the number of X's and O's on the board
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    # Determine whose turn it is 
    return 'O' if x_count > o_count else 'X'
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Return a set of positions (i, j) for all empty cells (None) on the board
    return {(i,j) for i in range(len(board)) for j in range (len(board[i])) if board [i][j] is None}

def result(board, action):
    """ 
    Returns the board that results from making move (i, j) on the board.
    """
    #  
    i,j = action 
    # Check if the specified cell is already occupied
    if board[i][j] is not None:
        raise ValueError (f"Invalid action: {action} Cell is already occupied")
    # Create a deep copy of the current board to avoid modifying the original board
    new_board = copy.deepcopy(board)
    # Replace the current player's symbol in the specified cell
    new_board[i][j] = player(board)
    # Return the new board state with the move applied
    return new_board
    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check every row and columns for a winner 
    for i in range (3):
        # Checking every row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Checking every column
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    # Checking diagonals for a winner 
    # Top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    # Top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    # No winner 
    return None 
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Return True if there's a winner or board is full (tie), False if game can continue
    return winner(board) is not None or not any (None in row for row in board)
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
     # Return score based on winner: +1 for X win, -1 for O win, 0 for tie
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the game is over, there are no valid moves
    if terminal(board):
        return None

    current_player = player(board)

    # Function for maximizing player's score 'X'
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    # Function for minimizing player's score 'O'
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v  

    # Find the action that leads to the highest minimum value
    if current_player == 'X':  
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value > best_value:
                best_value = move_value
                best_move = action
        return best_move
    # find the action that leads to lowest maximum value
    else:  
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value < best_value:
                best_value = move_value
                best_move = action
        return best_move
  
