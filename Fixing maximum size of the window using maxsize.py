from tkinter import *

root = Tk()

# Fixing the size of the root window.
# No one can now expand the size of the
# root window than the specified one.
root.maxsize(400, 200)

# Adding widgets to the root window
Label(root, text = 'Himel Sarder',
	font =('Verdana', 15)).pack(side = TOP, pady = 10)

Button(root, text = 'Click Me !').pack(side = TOP)

mainloop()


#Himel Sarder
#Dept of CSE, BSFMSTU
