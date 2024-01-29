'''
activebackground
-----------------
The background color when the mouse is over the radiobutton.

activeforeground
-----------------
The foreground color when the mouse is over the radiobutton.
'''

from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel, selectcolor="yellow", activebackground="red", activeforeground="white")
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel, selectcolor="yellow", activebackground="red", activeforeground="white")
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel, selectcolor="yellow", activebackground="red", activeforeground="white")
R3.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()
