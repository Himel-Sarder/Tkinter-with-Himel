'''The relief attribute is used to specify the appearance of the border around a widget. 
It takes various values that define the style of the border. Common values include:

"flat": No border.
"raised": Raised border.
"sunken": Sunken border.
"groove": Grooved border.
"ridge": Ridged border.
'''
from tkinter import Tk, Label

root = Tk()

# Create labels with different relief styles
label_flat = Label(root, text="Flat Relief", relief="flat")
label_flat.pack()

label_raised = Label(root, text="Raised Relief", relief="raised")
label_raised.pack()

label_sunken = Label(root, text="Sunken Relief", relief="sunken")
label_sunken.pack()

label_groove = Label(root, text="Groove Relief", relief="groove")
label_groove.pack()

label_ridge = Label(root, text="Ridge Relief", relief="ridge")
label_ridge.pack()

root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU
