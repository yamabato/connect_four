#encoding: utf-8

from tkinter import *
import tkinter.ttk as ttk
import tkMessageBox
import time

from board import ConnectFour
from com_players import *

first = ""
last = ""

first_name = ""
last_name = ""

kifu = []

piece_color = {
    0:"white",
    1:"blue",
    2:"red",
}

player_function = {
    "random_player":random_player,
    "hayabusa":hayabusa,
    "hayabusa2":hayabusa2,
    "hayabusa3":hayabusa3,
    "hayabusa4":hayabusa4,
    "hawk":hawk,
    "hawkC":hawkC,
}

com_player_list = (
    "random_player",
    "hayabusa","hayabusa2","hayabusa3","hayabusa4",
    "hawk","hawkC",
)

def start():
    global first,last,first_name,last_name,kifu

    p1 = player1_combo.get()
    p2 = player2_combo.get()

    player1_combo.configure(state="disable")
    player2_combo.configure(state="disable")

    first = p1
    last = p2

    if p1 in player_function:
        first = player_function[p1]
    if p2 in player_function:
        last = player_function[p2]

    first_name = p1
    last_name = p2

    board.__init__()
    kifu = []
    player_label.configure(text=first_name + " vs " + last_name)
    show()

    if not (isinstance(first,str) or isinstance(first,unicode)):
        click(-1)
    
def end(winner): 
    global kifu

    msg = "引き分け!"

    if winner == 0:
        msg = u"先手({0})の勝利".format(first_name)
    elif winner == 1:
        msg = u"後手({0})の勝利".format(last_name)
    elif winner == -1:
        msg = "試合中断"
    
    player1_combo.configure(state="normal")
    player2_combo.configure(state="normal")

    tkMessageBox.showinfo("Connect Four",msg)
    board.__init__()
    print kifu
    kifu = []
    show()

    turn_label.configure(text="試合待ち...")

def show():
    global kifu
    kifu.append(board.board)
    if board.turn % 2 == 0:
        turn_label.configure(text=u"先手番 {0}  思考中...".format(first_name))
    else:
        turn_label.configure(text=u"後手番 {0}  思考中...".format(last_name))

    for x in range(7):
        for y in range(6):
            piece = board.board[x][y]

            clr = piece_color[piece]

            canvas.create_oval(x*50,y*50,(x+1)*50,(y+1)*50,fill=clr,width=0)
    tk.update()

    board.show()

def click(x):
    global kifu

    player1_combo.configure(state="disable")
    player2_combo.configure(state="disable")

    x = x // 50    
    
    if x == -1:
        if board.turn % 2 ==0:
            board.drop(first(board,0))
        else:
            board.drop(last(board,1))

    elif board.turn % 2 == 0:
        if isinstance(first,str) or isinstance(first,unicode):
            board.drop(x)
        else:
            return
    else:
        if isinstance(last,str) or isinstance(last,unicode):
            board.drop(x)
        else:
            return

    canvas.delete(x_rect_id)
    canvas.delete(square_rect_id)
    show()
    
    result = board.judge()

    if result == 1:
        end(0)
        return 

    elif result == 2:
        end(1)
        return

    elif all(map(all,board.board)):
        end(-1)
        return

    if board.turn % 2 == 1 and not (isinstance(last,str) or isinstance(last,unicode)):
        click(-1)
    elif board.turn % 2 == 0 and not (isinstance(first,str) or isinstance(first,unicode)):
        click(-1)
        
def move(x):
    global x_rect_id,square_rect_id
    
    if board.turn % 2 == 0:
        if callable(first):
            return
    else:
        if callable(last):
            return

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

player1_combo = ttk.Combobox(tk, state="normal", width=20)
player1_combo["values"] = com_player_list
player1_combo.place(x=50,y=450)

player2_combo = ttk.Combobox(tk, state="normal", width=20)
player2_combo["values"] = com_player_list
player2_combo.place(x=50,y=470)

start_btn = Button(tk,text="試合開始",bg="blue",highlightbackground="blue",command=start)
start_btn.place(x=250,y=450)
end_btn = Button(tk,text="試合中断",bg="purple",highlightbackground="purple",command=lambda:end(-1))
end_btn.place(x=250,y=480)

exit_btn = Button(tk,text="終了",bg="red",highlightbackground="red",command=exit,font=("",20))
exit_btn.place(x=400,y=460)

for x in range(7):
    for y in range(6):
        canvas.create_oval(x*50,y*50,(x+1)*50,(y+1)*50,fill="white",width=0)

board = ConnectFour()
show()

canvas.bind("<ButtonPress>",lambda e: click(e.x))
canvas.bind("<Motion>",lambda e:move(e.x))

player1_combo.set("人間")
player2_combo.set("hawkC")
start()

tk.mainloop()

