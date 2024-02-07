from tkinter import *

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("New Window")

    label = Label(new_window, text="This is a new window!")
    label.pack()

# Create the main window
root = Tk()
root.title("Main Window")

# Create a button to open a new window
button = Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=20)

root.mainloop()
