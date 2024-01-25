from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Hello!! I am Himel")
    myLabel.pack()

myButton = Button(root, text="Click Me", padx=40, pady=20, command=myClick)  #padx increase weight
                                                                             #pady increase height
myButton.pack()

root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU
