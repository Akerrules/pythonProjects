
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
step=100

#draw column
for i in range(0, height, step): canvas.create_line(0,i,height,i)

#draw row
for i in range(0, width, step): canvas.create_line(i,0,i,width)

#ttk.Button(frame, text="quit", command=root.destroy).grid(column=1, row=3)

canvas.pack()
root.mainloop()