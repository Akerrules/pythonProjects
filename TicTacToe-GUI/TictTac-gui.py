
from tkinter import *
from tkinter import ttk
from tkinter import font

from numpy import pad


root= Tk()
root.geometry("300x400")
style = ttk.Style()

frame = ttk.Frame(root,padding=10)
#frame.grid()
style.configure("BW.TLabel", background="white")
style.configure("Test.TLabel", background="black", foreground = "white")
fontExample = font.Font(family="Arial", size=16, weight="bold", slant="italic")

canvas  = Canvas(root)
x,y,x2,y2=0,0,0,0
Frame_height, Frame_width = 400,300

#increment by 100
step=100

           #00  01  02   10  11  12    20  21  22
list_  = [["_","_","_"],["_","_","_"],["_","_","_"]]

pTurn = "X"
labelText = ttk.Label(root,text="Hello", style="Test.TLabel",font=fontExample )


isGameRunning = True
#when canvas is clicked
def callback(event):
    global pTurn, list_, isGameRunning
    if(isGameRunning):
        cords = calSquare(event.x,event.y)
        isLabeled = labelSquare(pTurn, int(cords[0]/step),int(cords[1]/step))

        #player Turn switch and draw image
        if(isLabeled and pTurn=="X"):
            ttk.Label(root,image=LabelImgX).place(x=cords[0]+10,y=cords[1]+10)
            pTurn = "O"
            labelText.config(text="O Turn")

        elif(isLabeled and pTurn=="O"):
            ttk.Label(root,image=LabelImgY).place(x=cords[0]+10,y=cords[1]+10)
            pTurn = "X"
            labelText.config(text="X Turn")

        #Display Winner status
        if(checkHor_Vert() or checkLeftDiagonal() or checkRightDiagonal()):
            if(pTurn=="X"):
                print("Player O won")
                labelText.config(text="O won")
            else:
                labelText.config(text="X won")
                print("X won")
            isGameRunning =False

  
    print(list_)

LabelImgX = PhotoImage(file="X.png", width=80,height=80)
LabelImgY = PhotoImage(file="O.png",width=80,height=80)

#draw column
for i in range(0, Frame_height, step): canvas.create_line(0,i,Frame_height,i,width=5)

#draw row
for i in range(0, Frame_width, step): canvas.create_line(i,0,i,Frame_width,width=5)


#ttk.Button(frame, text="quit", command=root.destroy).grid(column=1, row=3)

def calSquare(x,y):
   
    return (x-(x%step),y-(y%step))

flag = False

def checkHor_Vert():
    global flag
    for i in range(len(list_)):
        HorCheck = True
        VertCheck = True
        H = list_[i][0]
        V = list_[0][i]
        for j in range(len(list_)):
            if(list_[i][j] != (H) or H=="_"):
                print(list_[i][j])
                HorCheck =  False
            if(list_[j][i] != (V) or V=="_"):
                VertCheck  = False
        if(HorCheck or VertCheck):
            flag = True
    return flag

def checkLeftDiagonal():
    s = list_[0][0]
    for i in range(len(list_)):
        print(i,i)
        if(list_[i][i] != (s) or s=="_"):
            print(list_[i][i])
            return False
    print("left")
    return True

def checkRightDiagonal():
    counter = 0
    s= list_[2][0]
    for i in range(len(list_)-1,0,-1):
        print(counter,i)
        if(list_[counter][i] != (s) or s=="_"):
            print(list_[counter][i])
            return False
        counter = counter+1
    print("right")

    return True

def labelSquare(label, x,y):
    if list_[y][x] == ("_"):
        list_[y][x] = label
        return True
    return False
labelText.pack()
labelText.place(x=100,y=300,)

canvas.bind("<Button-1>", callback)
canvas.pack()
root.mainloop()