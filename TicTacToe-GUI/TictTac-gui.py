
from tkinter import *
from tkinter import ttk


root= Tk()
root.geometry("300x400")
frame = ttk.Frame(root,padding=10)
frame.grid()
ttk.Label(frame, text="Tic Tac Toe").grid(column=0, row = 0)
ttk.Button(frame, text="quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()