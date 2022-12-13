#!/usr/bin/env python
# coding: utf-8

# In[25]:


from random import choice
from math import inf

minmax_count = 0
abminmax_count = 0
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def Game_board(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for x in board:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n' + '---------------')
    print('===============')
    print('Next move')

def Clear_board(board):
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0

def winning_Player(board, player):
    conditions = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]]

    if [player, player, player] in conditions:
        return True

    return False

def game_Won(board):
    return winning_Player(board, 1) or winning_Player(board, -1)

def print_Result(board):
    if winning_Player(board, 1):
        print('X has won!, Alpha Beta Pruning  ' + '\n')
        print('No of nodes expanded by minmax is',minmax_count)
        print('No of nodes expanded by alpha beta pruning is',abminmax_count)

    elif winning_Player(board, -1):
        print('O\'s have won!, Min Max  ' + '\n')
        print('No of nodes expanded by minmax is',minmax_count)
        print('No of nodes expanded by alpha beta pruning is',abminmax_count)

    else:
        print('No more moves, Its a Draw' + '\n')
        print('No of nodes expanded by minmax is',minmax_count)
        print('No of nodes expanded by alpha beta pruning is',abminmax_count)

def blanks(board):
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])

    return blank

def board_Full(board):
    if len(blanks(board)) == 0:
        return True
    return False

def set_Move(board, x, y, player):
    board[x][y] = player

def get_Score(board):
    if winning_Player(board, 1):
        return 10

    elif winning_Player(board, -1):
        return -10

    else:
        return 0
    
def minimax(state, depth, player):
    global minmax_count
    minmax_count += 1
    if player == -1:
        best = [-1, -1, -inf]
    else:
        best = [-1, -1, +inf]

    if depth == 0 or game_Won(state):
        score = get_Score(state)
        return [-1, -1, score]

    for cell in blanks(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == -1:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

def abminimax(board, depth, alpha, beta, player):
    global abminmax_count
    abminmax_count += 1
    row = -1
    col = -1
    if depth == 0 or game_Won(board):
        return [row, col, get_Score(board)]

    else:
        for cell in blanks(board):
            set_Move(board, cell[0], cell[1], player)
            score = abminimax(board, depth - 1, alpha, beta, -player)
            if player == 1:
                # X is always the max player
                if score[2] > alpha:
                    alpha = score[2]
                    row = cell[0]
                    col = cell[1]

            else:
                if score[2] < beta:
                    beta = score[2]
                    row = cell[0]
                    col = cell[1]

            set_Move(board, cell[0], cell[1], 0)

            if alpha >= beta:
                break

        if player == 1:
            return [row, col, alpha]

        else:
            return [row, col, beta]

def o_comp(board):
    if len(blanks(board)) == 9:
        move = minimax(board, len(blanks(board)), -1)
        x, y = move[0], move[1]
        set_Move(board, x, y, -1)
        Game_board(board)

    else:
        result = abminimax(board, len(blanks(board)), -inf, inf, -1)
        set_Move(board, result[0], result[1], -1)
        Game_board(board)

def x_comp(board):
    if len(blanks(board)) == 9:
        move = minimax(board, len(blanks(board)), +1)
        x, y = move[0], move[1]
        set_Move(board, x, y, 1)
        Game_board(board)

    else:
        result = abminimax(board, len(blanks(board)), -inf, inf, 1)
        set_Move(board, result[0], result[1], 1)
        Game_board(board)

def make_Move(board, player, mode):
    if mode == 1:
        if player == 1:
            x_comp(board)
        else:
            o_comp(board)
    else:
        if player == 1:
            o_comp(board)
        else:
            x_comp(board)

def adver_search():
    current_Player = -1
    while not (board_Full(board) or game_Won(board)):
        make_Move(board, current_Player, 1)
        current_Player *= -1

    print_Result(board)

# Driver Code
print("=================================================")
print("TIC-TAC-TOE using MINIMAX with ALPHA-BETA Pruning")
print("=================================================")
adver_search()  


# In[ ]:




