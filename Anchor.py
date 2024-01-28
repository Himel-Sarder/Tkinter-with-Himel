from tkinter import *

root = Tk()

# Create label with anchor set to 'nw' (North-West)
label_nw = Label(root, text="Anchor NW", anchor="nw", width=20, height=5, borderwidth=1, relief="solid")
label_nw.grid(row=0, column=0)

# Create label with anchor set to 'center'
label_center = Label(root, text="Anchor Center", anchor="center", width=20, height=5, borderwidth=1, relief="solid")
label_center.grid(row=0, column=1)

# Create label with anchor set to 'se' (South-East)
label_se = Label(root, text="Anchor SE", anchor="se", width=20, height=5, borderwidth=1, relief="solid")
label_se.grid(row=1, column=0)

# Create label with anchor set to 'e' (South-East)
label_e = Label(root, text="Anchor E", anchor="e", width=20, height=5, borderwidth=1, relief="solid")
label_e.grid(row=1, column=1)

root.mainloop()
