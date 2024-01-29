from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Hello!! I am Himel", fg="Blue", bg="Yellow")    #fg = font color    #bg = background color
    myLabel.pack()

myButton = Button(root, text="Click Me", padx=40, pady=20, command=myClick, fg="Green", bg="Pink")
myButton.pack()

root.mainloop()


#Himel Sarder
#Dept. of CSE, BSFMSTU
