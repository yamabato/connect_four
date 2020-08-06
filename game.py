# encoding:utf-8

from board import ConnectFour

from com_player_tool import *
from hayabusa import *
from hawk import *
from swallow import *

first = "human"
last = swallow


while True:
    board = ConnectFour()

    print "!-*-対局開始!-*-!"

    print "人間" if first == "human" else first.__name__, "対", "人間" if last == "human" else last.__name__

    print

    board.show()
    for i in range(42):
        turn_str = "先手" if board.turn == 0 else "後手"

        if board.turn == 0:
            if first == "human":
                x = raw_input(turn_str + "の番(1~7): ")
            else:
                x = first(board, board.turn) + 1
        else:
            if last == "human":
                x = raw_input(turn_str + "の番(1~7): ")
            else:
                x = last(board, board.turn) + 1

        if x == "q":
            quit()

        print turn_str + "の手:", x

        if x != "" and str(x) in "1234567" and (not all(board.board[int(x) - 1])):
            print
            x = int(x) - 1
        else:
            print "反則により、" + turn_str + "の負け"
            print
            break

        board.drop(x)

        board.show()

        if board.judge() != 0:
            print turn_str + "の勝利!"
            print
            break
    else:
        print "引き分け!"
