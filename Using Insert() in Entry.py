from tkinter import *

root = Tk()

myEntry = Entry(root, bg="Orange", fg="Black", borderwidth=2)
myEntry.pack()
myEntry.insert(0, "Enter your name:")
def myClick():
    myLabel = Label(root, text="Hello " + myEntry.get() + "! Meet with Himel")
    myLabel.pack()

myButton = Button(root, text="Click", command=myClick, fg="Green", bg="Pink")
myButton.pack()

root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU
