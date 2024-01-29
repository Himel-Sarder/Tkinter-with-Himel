from tkinter import *
root = Tk()
root.title("Tkinter Status Bar Example")

def update_status_bar(message):
    status_var.set(message)

# Create a StringVar to store the status message
status_var = StringVar()

# Create a Label widget for the status bar
status_bar = Label(root, textvariable=status_var, bd=1, relief=SUNKEN, anchor=W)

# Pack the status bar to the bottom of the window
status_bar.pack(side=BOTTOM, fill=X)

# Update the status bar with a message
update_status_bar("Himel")

# Run the Tkinter event loop
root.mainloop()


'''
Let's break down the code:

1. `tk.StringVar()` is used to create a variable that can be associated with the `Label` widget. This variable will be updated to change the text displayed in the label.

2. `tk.Label()` creates a label widget that will serve as the status bar. It uses the `textvariable` parameter to associate the label's text with the `StringVar` created earlier. 
    The `bd` and `relief` parameters are used to add a border and a sunken appearance to the label, and `anchor=tk.W` aligns the text to the left.

3. `status_bar.pack(side=tk.BOTTOM, fill=tk.X)` packs the status bar to the bottom of the window and stretches it horizontally to fill the entire width.

4. The `update_status_bar` function is defined to update the status bar's text. You can call this function whenever you want to change the status message.

5. `update_status_bar("Ready")` initializes the status bar with the message "Himel"
'''
