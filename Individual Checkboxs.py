from tkinter import Tk, Checkbutton, Label, IntVar

def on_checkbox_change():
    # Update the label text based on checkbox states
    label.config(text=f"Checkbox 1: {var1.get()}, Checkbox 2: {var2.get()}")

root = Tk()
root.title("Himel's Checkboxes")

# Variables to store the state of each checkbox
var1 = IntVar()
var2 = IntVar()

# Create checkboxes
checkbox1 = Checkbutton(root, text="Checkbox 1", variable=var1, command=on_checkbox_change)
checkbox1.pack()

checkbox2 = Checkbutton(root, text="Checkbox 2", variable=var2, command=on_checkbox_change)
checkbox2.pack()

# Label to display the state of each checkbox
label = Label(root, text="Checkbox 1: 0, Checkbox 2: 0")
label.pack(pady=10)

root.mainloop()
