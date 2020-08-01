# encoding:utf-8

from board import ConnectFour
from com_players import *

first = hayabusa2
last = hayabusa3

first_win = 0
last_win = 0
draw = 0

N = 1000

print first.__name__, "vs", last.__name__

for i in range(N):
    print i + 1, "試合目"
    board = ConnectFour()

    for j in range(42):
        if board.turn == 0:
            x = first(board, board.turn)
        else:
            x = last(board, board.turn)

        board.drop(x)
        # board.show()

        if board.judge():
            if board.turn == 1:
                first_win += 1
            else:
                last_win += 1
            break
    else:
        draw += 1


print first.__name__, first_win, "勝"
print last.__name__, last_win, "勝"
print draw, "引き分け"
