import numpy as np
import copy

from Model.State import State


def North(i, j, board, turn):
    if (board[i - 1][j] == 0 or board[i - 1][j] == turn):
        return
    else:
        for k in range(i - 2, -1, -1):
            if (board[k][j] == 0):
                return [k, j]
            elif (board[k][j] == turn):
                return
            else:
                continue
        return


def East(i, j, board, turn):
    if (board[i][j + 1] == 0 or board[i][j + 1] == turn):
        return
    else:
        for k in range(j + 2, 8):
            if (board[i][k] == 0):
                return [i, k]
            elif (board[i][k] == turn):
                return
            else:
                continue
        return


def South(i, j, board, turn):
    if (board[i + 1][j] == 0 or board[i + 1][j] == turn):
        return
    else:
        for k in range(i + 2, 8):
            if (board[k][j] == 0):
                return [k, j]
            elif (board[k][j] == turn):
                return
            else:
                continue
        return


def West(i, j, board, turn):
    if (board[i][j - 1] == 0 or board[i][j - 1] == turn):
        return
    else:
        for k in range(j - 2, -1, -1):
            if (board[i][k] == 0):
                return [i, k]
            elif (board[i][k] == turn):
                return
            else:
                continue
        return


def NorthEast(i, j, board, turn):
    if (board[i - 1][j + 1] == 0 or board[i - 1][j + 1] == turn):
        return
    else:
        for k1 in range(i - 2, -1, -1):
            for k2 in range(j + 2, 8):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return


def SouthEast(i, j, board, turn):
    if (board[i + 1][j + 1] == 0 or board[i + 1][j + 1] == turn):
        return
    else:
        for k1 in range(i + 2, 8):
            for k2 in range(j + 2, 8):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return


def SouthWest(i, j, board, turn):
    if (board[i + 1][j - 1] == 0 or board[i + 1][j - 1] == turn):
        return
    else:
        for k1 in range(i + 2, 8):
            for k2 in range(j - 2, -1, -1):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return


def NorthWest(i, j, board, turn):
    if (board[i - 1][j - 1] == 0 or board[i - 1][j - 1] == turn):
        return
    else:
        for k1 in range(i - 2, -1, -1):
            for k2 in range(j - 2, -1, -1):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return

def possible(board, i, j, turn):
    tbr = []
    tbr.append(North(i,j,board,turn))
    tbr.append(East(i, j, board, turn))
    tbr.append(South(i, j, board, turn))
    tbr.append(West(i, j, board, turn))
    tbr.append(NorthEast(i, j, board, turn))
    tbr.append(SouthEast(i, j, board, turn))
    tbr.append(SouthWest(i, j, board, turn))
    tbr.append(NorthWest(i, j, board, turn))
    return tbr

def flip(board, possible_pos):
    temp = copy.deepcopy(board)
    #
    #
    state = State(temp)


def Next(state, turn):
    state_array = []
    board = state.Board
    for i in range(0, 8):
        for j in range(0, 8):
            if (board[i][j] == turn):
                possible_pos = possible(board, i, j, turn)
                new_states = flip(board, possible_pos)
                np.concatenate(state_array, new_states)

    return state_array