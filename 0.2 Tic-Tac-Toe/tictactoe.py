"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_counter = 0
    o_counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x_counter += 1
            elif board[i][j] == "O":
                o_counter += 1
    
    if x_counter > o_counter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avilable_actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                avilable_actions.add( (i, j) )
    
    return avilable_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tmp_board = copy.deepcopy(board)
    turn = player(board)
    i = action[0]
    j = action[1]
    
    tmp_board[i][j] = turn
    return tmp_board

    
def winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[i][0] != EMPTY:
            return board[0][i]
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[i][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[i][0] != EMPTY:
        return board[0][2]
    
    return "TIE"       


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    isWin = winner(board)
    if isWin == X or isWin == O:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    
    if(terminal(board)):
        return None            
    
    # tmp_board = []
    
    # for i in range(3):
    #     tmp_list = []
    #     for j in range(3):
    #         tmp_list.append(board[i][j])
    #     tmp_board.append(tmp_list)

    
    def Min_value(board):
        if terminal(board):
            return utility(board)
        
        v = 999999999
        
        for action in actions(board):
            v = min(v, Max_value(result(board, action)))
        return v
    
    def Max_value(board):
        if terminal(board):
            return utility(board)
        
        v = -999999999
        for action in actions(board):
            v = max(v, Min_value(result(board, action)))
        return v
    
    best_action = (0,0)
    current_player = player(board)
    
    if current_player == X:
        MAX = -999999999
        for action in actions(board):
            tmp_max =  Max_value(result(board, action))
            if tmp_max >= MAX:
                best_action = action 
                
    elif current_player == O:
        MIN = 999999999
        for action in actions(board):
            tmp_min =  Min_value(result(board, action))
            if tmp_min <= MIN:
                best_action = action 
                
    return best_action
