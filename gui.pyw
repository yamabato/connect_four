#encoding: utf-8

from tkinter import *
import tkMessageBox
import time

from board import ConnectFour
from com_players import *

first = hawk
last = "human"

piece_color = {
    0:"white",
    1:"blue",
    2:"red",
}

def show():
    for x in range(7):
        for y in range(6):
            piece = board.board[x][y]

            clr = piece_color[piece]

            canvas.create_oval(x*50,y*50,(x+1)*50,(y+1)*50,fill=clr,width=0)
    tk.update()

def click(x):
    x = x // 50    
    
    if x == -1:
        if board.turn % 2 ==0:
            board.drop(first(board,0))
        else:
            board.drop(last(board,1))

    elif board.turn % 2 == 0:
        if first == "human":
            board.drop(x)
        else:
            board.drop(first(board,0))
    else:
        if last == "human":
            board.drop(x)
        else:
            board.drop(last(board,1))

    show()
    
    result = board.judge()

    if result == 1:
        tkMessageBox.showinfo("Connect Four","先手の勝利")
        board.__init__()
        show()
        if first != "human":
            click(-1)
        return

    elif result == 2:
        tkMessageBox.showinfo("Connect Four","後手の勝利")
        board.__init__()
        show()
        if first != "human":
            click(-1)
        return

    elif all(map(all,board.board)):
        tkMessageBox.showinfo("Connect Four","引き分け!")
        board.__init__()
        show()
        if first != "human":
            click(-1)
        return

    if board.turn % 2 == 1 and last != "human":
        click(-1)
    elif board.turn % 2 == 0 and first != "human":
        click(-1)
        

tk = Tk()
tk.title("Connect Four")
tk.geometry("500x500")

canvas = Canvas(tk,height=300,width=350,bg="#696969")
canvas.place(x=50,y=50)

for x in range(7):
    for y in range(6):
        canvas.create_oval(x*50,y*50,(x+1)*50,(y+1)*50,fill="white",width=0)

board = ConnectFour()

canvas.bind("<ButtonPress>",lambda e: click(e.x))

if first != "human":
    click(-1)

tk.mainloop()

