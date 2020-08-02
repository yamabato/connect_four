from board import ConnectFour
from com_players import *

board = ConnectFour()

"""
board.board = [
    [2, 2, 2, 1, 1, 1],
    [2, 2, 1, 2, 1, 2],
    [0, 0, 0, 0, 0, 1],
    [2, 1, 1, 2, 1, 2],
    [1, 1, 1, 2, 2, 1],
    [0, 0, 0, 0, 0, 2],
    [2, 1, 1, 2, 2, 1],
]
"""

board.show()
print hawk(board, 1)
