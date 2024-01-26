from tkinter import *

root = Tk()
root.title("Himel's Calculator")



myEntry = Entry(root, bd=2, width=20)
myEntry.grid(row=0, column=0, columnspan=3)  # Span across three columns

myEntry2 = Entry(root, bd=2, width=20)
myEntry2.grid(row=0, column=4, rowspan=3)  # span across three rowspan



myButton1 = Button(root, text="1", padx=13, pady=10)
myButton2 = Button(root, text="2", padx=13, pady=10)
myButton3 = Button(root, text="3", padx=13, pady=10)

myButton1.grid(row=1, column=1)
myButton2.grid(row=1, column=2)
myButton3.grid(row=1, column=3)

root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU
