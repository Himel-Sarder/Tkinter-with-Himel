from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="This is a long text for Option 1", variable=var, value=1, command=sel, selectcolor="yellow", activebackground="lightblue", wraplength=100)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2 with a longer text that will be wrapped onto the next line", variable=var, value=2, command=sel, selectcolor="yellow", activebackground="lightblue", wraplength=150)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel, selectcolor="yellow", activebackground="lightblue")
R3.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()


'''
The wraplength option is set to limit the number of pixels for text wrapping. 
For example, wraplength=100 limits the text in the first Radiobutton to wrap onto the next line after 100 pixels.
The default value is wraplength=0, which means that lines will be broken only at newlines.
'''

#Himel Sarder
#Dept. of CSE, BSFMSTU
