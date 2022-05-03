


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
Frame_height, Frame_width = 400,300

#increment by 100
step=100
list_  = [["_","_","_"],["_","_","_"],["_","_","_"]]
pTurn = "X"

#when canvas is clicked
def callback(event):
    global pTurn, list_
    cords = calSquare(event.x,event.y)
    isLabeled = labelSquare(pTurn, int(cords[0]/step),int(cords[1]/step))

    #player Turn switch and draw image
    if(isLabeled and pTurn=="X"):
        Label(root,image=LabelImgX).place(x=cords[0],y=cords[1])
        pTurn = "O"
    elif(isLabeled and pTurn=="O"):
        Label(root,image=LabelImgY).place(x=cords[0],y=cords[1])
        pTurn = "X"
    print(list_)

LabelImgX = PhotoImage(file="X.png")
LabelImgY = PhotoImage(file="O.png")
labelX = Label(root,image=LabelImgX)
labelX.place(x=0,y=0)



#draw column
for i in range(0, Frame_height, step): canvas.create_line(0,i,Frame_height,i,width=5)

#draw row
for i in range(0, Frame_width, step): canvas.create_line(i,0,i,Frame_width,width=5)
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