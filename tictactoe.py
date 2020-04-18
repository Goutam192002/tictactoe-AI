"""
Tic Tac Toe Player
"""
import copy
import random

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
    number_of_x = 0
    number_of_o = 0
    for row in board:
        for column in row:
            if column == "X":
                number_of_x += 1
            elif column == "O":
                number_of_o += 1
    if number_of_x > number_of_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    current_player = player(new_board)
    new_board[action[0]][action[1]] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i, row in enumerate(board):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    for j, column in enumerate(board):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for column in row:
            if column is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)
    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_moves = actions(board)
    random.shuffle(possible_moves)
    best_move = None
    fronteir = []
    best_value = 0
    for move in possible_moves:
        best_move = move
        resulting_board = result(board, move)
        if terminal(resulting_board) and utility(board) >= -1:
            return best_move
        else:
            if player(board) == X:
                fronteir.append((move, minvalue(resulting_board)))
            else:
                fronteir.append((move, maxvalue(resulting_board)))
    for node in fronteir:
        if player(board) == X:
            if node[1] >= best_value:
                return node[0]
        else:
            if node[1] <= best_value:
                return node[0]


def maxvalue(board):
    value = -2
    if terminal(board):
        return utility(board)
    else:
        possible_moves = actions(board)
        random.shuffle(possible_moves)
        for move in possible_moves:
            resulting_board = result(board, move)
            resulting_value = minvalue(resulting_board)
            if resulting_value > value:
                value = resulting_value
        return value


def minvalue(board):
    value = 2
    if terminal(board):
        return utility(board)
    else:
        possible_moves = actions(board)
        random.shuffle(possible_moves)
        for move in possible_moves:
            resulting_board = result(board, move)
            resulting_value = maxvalue(resulting_board)
            if resulting_value < value:
                value = resulting_value
        return value
