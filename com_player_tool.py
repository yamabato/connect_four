# encoding:utf-8

import random
from collections import Counter


def random_player(board, hand):
    possible = []

    for i in range(7):
        if not all(board.board[i]):
            possible.append(i)

    return random.choice(possible)


def legal_hands(board):
    legal = []
    for i in range(7):
        if not all(board.board[i]):
            legal.append(i)

    return legal


def evaluation(board, hand):
    sign = "1" if hand == 0 else "2"

    clear_line = str(sign) * 4
    check_lines = [
        "0" + str(sign) * 3,
        str(sign) + "0" + str(sign) * 2,
        str(sign) * 2 + "0" + str(sign),
        str(sign) * 3 + "0",
    ]

    clear_point = 2
    check_point = 1

    point = 0

    board_flat = []
    for y in range(6):
        for x in range(7):
            board_flat.append(board.board[x][y])

    for l in board.lines:
        line = ""
        for n in l:
            line += str(board_flat[n])

        if clear_line in line:
            point += clear_point

        for c in check_lines:
            if c in line:
                point += check_point

    return point
