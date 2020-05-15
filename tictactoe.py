"""
Tic Tac Toe Player
"""

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
    count = 0
    for row in board:
        for column in row:
            if column is not None:
                count+=1

    if count%2==0:
        return X
    else:
        return O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i,row in enumerate(board):
        for j,elem in enumerate(row):
            if elem is EMPTY:
                moves.append((i,j))
    return moves    
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    (i,j) = action
    resultant_board=[]
    for row in board:
        r=[]
        for col in row:
            r.append(col)
        resultant_board.append(r)
    if resultant_board[i][j] is EMPTY:
        resultant_board[i][j]=current_player
        return resultant_board
    else:
        print(i,j)
        # raise Exception ("Invalid Move")
    return resultant_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    prim_diagnol_elem=[]
    sec_diagnol_elem=[]
    for i,row in enumerate(board):
        if all(elem == row[0] for elem in row) and row[0] is not EMPTY:
            return row[0]
        prim_diagnol_elem.append(row[i])
        sec_diagnol_elem.append(row[2-i])
        for j,col in enumerate(row):
            elem = board[0][i]
            if board[j][i] is not elem:
                break
            elif j==2:
                return elem 
    
    if all(elem == prim_diagnol_elem[0] for elem in prim_diagnol_elem):
        return prim_diagnol_elem[0]

    if all(elem == sec_diagnol_elem[0] for elem in sec_diagnol_elem):
        return sec_diagnol_elem[0]

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i,row in enumerate(board):
        if any(elem is EMPTY for elem in row):
            break
        if i==2:
            return True
    if winner(board) is not None:
        return True
    else:
        return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) is X:
        v=-1000000
        i = -1
        j = -1
        for action in actions(board):
            action_value = min_value(result(board,action))
            if v < action_value:
                v = action_value
                (i,j)=action
        return (i,j)
    elif player(board) is O:
        v=1000000
        i=-1
        j=-1
        for action in actions(board):
            action_value = max_value(result(board,action))
            if v > action_value:
                v = action_value
                (i,j)=action
        return (i,j)
    else:
        return None

    # raise NotImplementedError

def max_value(board):
    if terminal(board):
        return utility(board)
    v=-10000
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v=10000
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v