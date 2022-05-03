

from msilib.schema import SelfReg
from tkinter import *
from tkinter import ttk





root= Tk()
root.geometry("300x400")
style = ttk.Style()
frame = ttk.Frame(root,padding=10)
#frame.grid()
style.configure("BW.TLabel", background="white")
canvas  = Canvas(root)


x,y,x2,y2=0,0,0,0
height, width = 400,300

#increment by 100
step=100
list_  = [["_","_","_"],["_","_","_"],["_","_","_"]]
pTurn = "X"

def callback(event):
    global pTurn, list_
    cords = calSquare(event.x,event.y)
    isLabeled = labelSquare(pTurn, int(cords[0]/step),int(cords[1]/step))
    #player Turn switch
    if(isLabeled and pTurn=="X"):
        pTurn = "O"
    elif(isLabeled and pTurn=="O"):
        pTurn = "X"

    print(list_)

#draw column
for i in range(0, height, step): canvas.create_line(0,i,height,i)

#draw row
for i in range(0, width, step): canvas.create_line(i,0,i,width)
    #       00  01  02   10  11  12     20  21  22


#ttk.Button(frame, text="quit", command=root.destroy).grid(column=1, row=3)

def calSquare(x,y):
   
    return (x-(x%step),y-(y%step))

def checkWinnerHorizontal(x,y):
    for i in range(len(list_)):
        isWinner =True
        for j in range(len(list_)):
            s = list[i][j]
            if(list[i][j] == (s) and isWinner):
                isWinner =False


def labelSquare(label, x,y):
    if list_[y][x] == ("_"):
        list_[y][x] = label
        return True
    return False
    
canvas.bind("<Button-1>", callback)

canvas.pack()
root.mainloop()