from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel, selectcolor="yellow", activebackground="lightblue", underline=1)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel, selectcolor="yellow", activebackground="lightblue", underline=-1)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel, selectcolor="yellow", activebackground="lightblue", underline=5)
R3.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()

'''
The text for each Radiobutton contains an underscore (_) at a specific position to indicate underlining.
The underline option is set to the position of the underscore in the text (counting from 0). 
For example, underline=1 means that the letter at position 1 (the second letter) will be underlined.
The default value is underline=-1, which means no underlining.
'''
