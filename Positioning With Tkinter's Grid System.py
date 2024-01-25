from tkinter import *

root = Tk()

myL1 = Label(root, text="Hello World")
myL2 = Label(root, text="My name is Himel")
myL1.grid(row=0, column=0)
myL2.grid(row=1, column=0)

root.mainloop()

-----------
Another Way
-----------

from tkinter import *

root = Tk()

myL1 = Label(root, text="Hello World").grid(row=0, column=0)
myL2 = Label(root, text="My name is Himel").grid(row=1, column=0)

root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU
