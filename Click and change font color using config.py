from tkinter import Tk, Label, Button

def change_text_color():
    label.config(fg="blue")

root = Tk()
root.title("Config Example")

# Initial Label widget
label = Label(root, text="Hello, Himel!", fg="black")
label.pack(pady=20)

# Button to change text color dynamically
change_color_button = Button(root, text="Change Text Color", command=change_text_color)
change_color_button.pack(pady=10)

root.mainloop()
