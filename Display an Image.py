from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.maxsize(400, 200)
root.minsize(400, 200)

Label(root, text='Himel Sarder', font=('Verdana', 15)).pack(side=TOP, pady=10)

# Open the image file and create a PhotoImage object
myimage = ImageTk.PhotoImage(Image.open("Himel.jpg"))

# Create a Label to display the image
imagelabel = Label(root, image=myimage)
imagelabel.pack()

root.mainloop()

#Himek Sarder
#Dept of CSE, BSFMSTU
