from tkinter import ttk
from tkinter import *

root  = Tk()


width = 500
height  = 500
root.geometry("500x500")
style = ttk.Style()
frame = ttk.Frame(root,padding=10)
root.title("Aker's MemoryTest")

canvas  = Canvas(root)
canvas.config(width=500,height=500)

grid =500
level = 250
counter =0
for i in range(0,grid,level):
    for j in range(0,grid,level):
        canvas.create_line(j, 0, j, height,width=5)
        canvas.create_line(0, j, width,j, width=5)
        counter= counter+1


canvas.pack()
root.mainloop()
