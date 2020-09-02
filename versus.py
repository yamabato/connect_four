# encoding:utf-8
import sys

from board import ConnectFour

from com_player_tool import *
from hayabusa import *
from hawk import *
from swallow import *

def versus(first,last,N):
    first_win = 0
    last_win = 0
    draw = 0

    print first.__name__, "vs", last.__name__

    for i in range(N):
        percent = float(i+1) / float(N) * 100

        #if percent == int(percent):
        sys.stdout.write("\r" + "#"*int(percent/2) + "  " + str(percent)+"%  " + str(i+1) + "/" + str(N))
        sys.stdout.flush()

        board = ConnectFour()

        for j in range(42):
            if board.turn == 0:
                x = first(board, board.turn)
            else:
                x = last(board, board.turn)

            board.drop(x)

            if board.judge():
                if board.turn == 1:
                    first_win += 1
                else:
                    last_win += 1
                break
        else:
            draw += 1

    print ""
    print first.__name__, first_win, "勝"
    print last.__name__, last_win, "勝"
    print draw, "引き分け"

versus(swallow,bosatsu,100)
