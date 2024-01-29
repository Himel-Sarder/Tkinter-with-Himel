from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel, selectcolor="yellow", activebackground="lightblue", cursor="arrow")
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel, selectcolor="yellow", activebackground="lightblue", cursor="dot")
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel, selectcolor="yellow", activebackground="lightblue", cursor="plus")
R3.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()
