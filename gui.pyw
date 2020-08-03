#encoding: utf-8

from tkinter import *
import tkMessageBox
import time

from board import ConnectFour
from com_players import *

first = "人間代表"
last = hawk

first_name =first if type(first) == str else first.__name__
last_name = last if type(last) == str else last.__name__

kifu = []

piece_color = {
    0:"white",
    1:"blue",
    2:"red",
}

def show():
    global kifu
    kifu.append(board.board)
    if board.turn % 2 == 0:
        turn_label.configure(text="先手番 "+first_name + "  思考中...")
    else:
        turn_label.configure(text="後手番 "+last_name + "  思考中...")

    for x in range(7):
        for y in range(6):
            piece = board.board[x][y]

            clr = piece_color[piece]

            canvas.create_oval(x*50,y*50,(x+1)*50,(y+1)*50,fill=clr,width=0)
    tk.update()

    board.show()
def click(x):
    global kifu
    x = x // 50    
    
    if x == -1:
        if board.turn % 2 ==0:
            board.drop(first(board,0))
        else:
            board.drop(last(board,1))

    elif board.turn % 2 == 0:
        if type(first) == str:
            board.drop(x)
        else:
            board.drop(first(board,0))
    else:
        if type(last) == str:
            board.drop(x)
        else:
            board.drop(last(board,1))

    canvas.delete(x_rect_id)
    canvas.delete(square_rect_id)
    show()
    
    result = board.judge()

    if result == 1:
        tkMessageBox.showinfo("Connect Four","先手"+first_name+"の勝利")
        board.__init__()
        show()
        if type(first) != str:
            click(-1)
        print kifu
        kifu = []
        return

    elif result == 2:
        tkMessageBox.showinfo("Connect Four","後手"+last_name+"の勝利")
        board.__init__()
        show()
        if type(first) != str:
            click(-1)
        print kifu
        kifu = []
        return

    elif all(map(all,board.board)):
        tkMessageBox.showinfo("Connect Four","引き分け!")
        board.__init__()
        show()
        if type(first) != str:
            click(-1)
        print kifu
        kifu = []
        return

    if board.turn % 2 == 1 and type(last) != str:
        click(-1)
    elif board.turn % 2 == 0 and type(first) != str:
        click(-1)
        
def move(x):
    global x_rect_id,square_rect_id
    
    if x_rect_id != -1:
        canvas.delete(x_rect_id)
    if square_rect_id != -1:
        canvas.delete(square_rect_id)
    
    line_x = (x//50)*50
    x_rect_id = canvas.create_rectangle(line_x,0,line_x+50,300,width=2)
    
    if x//50 < 7 and  not all(board.board[x//50]):
        y = board.board[x//50].count(0)*50
        square_rect_id = canvas.create_oval(line_x,y-50,line_x+50,y,width=0,stipple="gray50",fill="gray")

tk = Tk()
tk.title("Connect Four")
tk.geometry("500x500")
tk.configure(bg="#8d6449")

canvas = Canvas(tk,height=300,width=350,bg="#696969")
canvas.place(x=50,y=50)

x_rect_id = -1
square_rect_id = -1

turn_label = Label(tk,text="先手番",font=("",30))
turn_label.place(x=0,y=0)
player_label = Label(tk,text=first_name + " vs " + last_name,font=("",20))
player_label.place(x=50,y=380)

for x in range(7):
    for y in range(6):
        canvas.create_oval(x*50,y*50,(x+1)*50,(y+1)*50,fill="white",width=0)

board = ConnectFour()
show()

canvas.bind("<ButtonPress>",lambda e: click(e.x))
canvas.bind("<Motion>",lambda e:move(e.x))

if type(first) != str:
    click(-1)

tk.mainloop()

