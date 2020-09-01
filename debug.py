from board import ConnectFour

from com_player_tool import *
from hayabusa import *
from hawk import *
from swallow import *

board = ConnectFour()

board.board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
kifu = [3, 4, 4, 3, 3, 4, 4, 4, 3, 3, 1, 4, 3, 0, 5, 6, 1, 1, 5, 1, 0, 0, 0]

for x in kifu:
    board.drop(x)

board.show()
print swallow(board,1)
