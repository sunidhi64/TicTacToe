"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return  O if x_count > o_count else X
    

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_moves.add((row, col))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    copy_board = np.array(board)
    win = [check_for_row(copy_board), check_for_col(copy_board), check_for_diagonal(copy_board)]
    if X in win:
        return X
    elif O in win:
        return O
    else:
        return None

def check_for_row(board):
    for i in range(board.shape[0]):
        if np.all(board[i] == X):
            return X
        if np.all(board[i] == O):
            return O
    return EMPTY

def check_for_col(board):
    trans_board = board.T
    for i in range(trans_board.shape[0]):
        if np.all(trans_board[i] == X):
            return X
        if np.all(trans_board[i] == O):
            return O
    return EMPTY

def check_for_diagonal(board):
    main_diagonal = board.diagonal()
    anti_diagonal = np.fliplr(board).diagonal() 
    if all([i == X for i in main_diagonal]) or all([i == X for i in anti_diagonal]):
        return X
    elif all([i == O for i in main_diagonal]) or all([i == O for i in anti_diagonal]):
        return O
    else:
        return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = {X : 1, O : -1, None : 0}
    return win[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        v, move = max_value(board)
        return move

    else:
        v, move = min_value(board)
        return move

def max_value(board):
    v = float('-inf')
    if terminal(board):
        return utility(board), None
    move = None
    for action in actions(board):
        val, mv = min_value(result(board, action))
        if val > v:
            move = action
            v = val
            if v == 1:
                return v, move
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    move = None
    for action in actions(board):
        val, mv = max_value(result(board, action))
        if v > val:
            v = val
            move = action
            if v == -1:
                return v, move
    return v, move




    
    

