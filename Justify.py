from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="Option 1\nMultiple Lines", variable=var, value=1, command=sel, selectcolor="yellow", activebackground="lightblue", justify=LEFT)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2\nMultiple Lines", variable=var, value=2, command=sel, selectcolor="yellow", activebackground="lightblue", justify=CENTER)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3\nMultiple Lines", variable=var, value=3, command=sel, selectcolor="yellow", activebackground="lightblue", justify=RIGHT)
R3.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()

'''
The state=NORMAL
----------------
                is the default state, where the radiobutton is responsive.

The state=ACTIVE
----------------
                is the state when the cursor is currently over the radiobutton. This state is automatically activated when the cursor hovers over the widget.

The state=DISABLED
------------------
                is used to gray out the control and make it unresponsive. 


In the example, I initially set R2 to be disabled.
'''

#Himel Sarder
#Dept. of CSE, BSFMSTU
