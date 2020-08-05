# encoding:utf-8

import random
import itertools
import copy

from board import ConnectFour
from com_player_tool import *
from hawk import check


def swallow(board, hand):
    check_x, option = check(board, hand)

    if check_x != -1:
        return check_x

    legal = legal_hands(board)
    original_board = copy.deepcopy(board.board)

    for x in legal:
        pass
