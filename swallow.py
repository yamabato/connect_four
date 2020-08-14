# encoding:utf-8

import sys
import random
import itertools
import copy

from board import ConnectFour
from com_player_tool import *
from hawk import check

def random_alpha(board,hand):
    check_x, option = check(board,hand)
    if check_x != -1:
        return check_x
    if option:
        return random.choice(option)
    return random.choice(legal_hands(board))

def swallow_engine(board, hand,f,trials,do_check,print_info):
    if do_check:
        check_x, option = check(board, hand)
    else:
        check_x = -1
        option = legal_hands(board)

    legal = legal_hands(board)
    original_board = copy.deepcopy(board.board)

    wins = {k:0 for k in legal}

    player = f

    for x in legal:
        for i in range(trials):
            board.board = copy.deepcopy(original_board)
            board.turn = hand

            board.drop(x)

            while True:
                if all(map(all,board.board)):
                    break

                board.drop(player(board,board.turn))
                
                result = board.judge()
                if result == 1:
                    if hand == 0:
                        wins[x] += 1
                    break
                elif result == 2:
                    if hand == 1:
                        wins[x] += 1
                    break

    board.board = original_board
    board.turn = hand

    choiced = [-1,[]]

    for x in wins.keys():
        value = wins[x]
        if choiced[0] < value:
            choiced = [value,[x]]
        elif choiced[0] == value:
            choiced[1].append(x)
    
    choiced_x = -1

    if check_x != -1:
        choiced_x = check_x
    elif choiced[1]:
        choiced_x = random.choice(choiced[1])
    else:
        if legal:
            choiced_x = random.choice(legal)
        else:
            return -1

    #情報表示部 
    if print_info:
        print "先手番" if hand == 0 else "後手番"
        [sys.stdout.write(str(k)+": "+str(round(float(wins[k]) / float(trials) * 100,2))+"%\n") for k in wins.keys()]
        print "選択:",choiced_x
        print "想定勝率:", (float(wins[choiced_x])/float(trials))*100,"%\n"
    
    return choiced_x

def swallow(board,hand):
    return swallow_engine(board,hand,random_alpha,100,True,True)

def swallow_fast(board,hand):
    return swallow_engine(board,hand,random_player,50,True,True)

def swallow_powerful(board,hand):
    return swallow_engine(board,hand,random_alpha,200,True,True)

def swallowC(board,hand):
    return swallow_engine(board,hand,random_alpha,100,False,True)
