"""
Tic Tac Toe Player
"""

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # FIX: comparison operator and correct logic
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("Invalid action: out of bounds")

    if board[i][j] != EMPTY:
        raise Exception("Invalid action: cell already occupied")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    lines = []

    for i in range(3):
        lines.append(board[i])

    for j in range(3):
        lines.append([board[0][j], board[1][j], board[2][j]])

    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]

    return None


def terminal(board):
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    w = winner(board)

    if w == X:
        return 1
    if w == O:
        return -1
    return 0


# ---------------- MINIMAX ENGINE (ADDED, NOT REWRITTEN) ---------------- #

def max_value(board):
    if terminal(board):
        return utility(board)

    value = float("-inf")
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    if terminal(board):
        return utility(board)

    value = float("inf")
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # FIX: terminal case must return None (not utility)
    if terminal(board):
        return None

    if player(board) == X:
        best_value = float("-inf")
        best_move = None
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_value:
                best_value = val
                best_move = action
        return best_move
    else:
        best_value = float("inf")
        best_move = None
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_value:
                best_value = val
                best_move = action
        return best_move
