# encoding:utf-8

import sys
import random
import itertools
import copy
import collections

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

def swallow_play_out(board,hand,f,trials,legal):
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

    return wins

def swallow_engine(board, hand,f,trials,do_check,print_info,choice_x_func):
    if do_check:
        check_x, option = check(board, hand)
        if not option:
            print "0%"
            return legal_hands(board)[0]
    else:
        check_x = -1
        option = legal_hands(board)
    
    wins = swallow_play_out(board,hand,f,trials,option)
    wins["all"] = trials
    
    if check_x == -1:
        choiced_x = choice_x_func(wins,option)
    else:
        choiced_x = check_x

    if choiced_x == -1:
        return -1

    #情報表示部 
    if print_info:
        show_info(wins,trials,choiced_x,hand)
    
    return choiced_x

def choice_x_win(wins,legal):
    choiced = [-1,[]]

    for x in legal:
        value = wins[x]
        if choiced[0] < value:
            choiced = [value,[x]]
        elif choiced[0] == value:
            choiced[1].append(x)
    
    choiced_x = -1

    if choiced[1]:
        choiced_x = random.choice(choiced[1])
    else:
        if legal:
            choiced_x = random.choice(legal)
        else:
            return -1

    return choiced_x


def choice_x_draw(wins,legal):
    choiced = [100,[]]

    for x in legal:
        value = abs((float(wins[x]) / float(wins["all"]) * 100)-50)
        if choiced[0] > value:
            choiced = [value,[x]]
        elif choiced[0] == value:
            choiced[1].append(x)
    
    choiced_x = -1

    if choiced[1]:
        choiced_x = random.choice(choiced[1])
    else:
        if legal:
            choiced_x = random.choice(legal)
        else:
            return -1

    return choiced_x


def show_info(wins,trials,choiced_x,hand):
    wins = {k:wins[k] for k in filter(lambda x:x!="all",wins.keys())}
    print "\033[41m先手番\033[0m" if hand == 0 else "\033[44m後手番\033[0m"
    [sys.stdout.write(str(k)+": "+ ("\033[31m" if round(float(wins[k]) / float(trials) * 100,2) < 50 else "\033[34m") +str(round(float(wins[k]) / float(trials) * 100,2))+"%\033[0m\n") for k in wins.keys()]
    
    win_rate = (float(wins[choiced_x])/float(trials))*100
    clr = "\033[31m" if win_rate < 50 else "\033[34m"
    print "選択:", clr + str(choiced_x) + "\033[0m"
    print "想定勝率:", clr + str(win_rate),"%\n\033[0m"

def swallow(board,hand):
    return swallow_engine(board,hand,random_alpha,100,True,True,choice_x_win)

def swallow_fast(board,hand):
    return swallow_engine(board,hand,random_player,50,True,False,choice_x_win)

def swallow_powerful(board,hand):
    return swallow_engine(board,hand,random_alpha,200,True,True,choice_x_win)

def swallowC(board,hand):
    return swallow_engine(board,hand,random_alpha,100,False,True,choice_x_win)

def swallowW(board,hand):
    return swallow_engine(board,hand,random_player,20,False,False,choice_x_win)

def swallowD(board,hand):
    return swallow_engine(board,hand,random_alpha,100,True,True,choice_x_draw)

def bosatsu(board,hand):
    choiced = [swallow_fast(board,hand),swallow_fast(board,hand),swallow_fast(board,hand)]
    #print sorted(choiced)
    return collections.Counter(choiced).most_common()[0][0]


