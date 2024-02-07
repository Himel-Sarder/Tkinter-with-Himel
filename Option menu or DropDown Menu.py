from tkinter import Tk, StringVar, OptionMenu, Label

def on_option_change():
    selected_option = selected_var.get()
    label.config(text=f"Selected Option: {selected_option}")

root = Tk()
root.title("Option Menu Example")

# List of options for the option menu
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Variable to store the selected option
selected_var = StringVar()
selected_var.set(options[0])  # Set the default selected option

# Create an OptionMenu
option_menu = OptionMenu(root, selected_var, *options, command=on_option_change)
option_menu.pack(pady=20)

# Label to display the selected option
label = Label(root, text="Selected Option: ")
label.pack()

root.mainloop()
