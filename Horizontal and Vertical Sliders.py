from tkinter import Tk, Scale, Label, HORIZONTAL, VERTICAL



def on_horizontal_change(value):
    horizontal_label.config(text=f"Horizontal Value: {value}")

def on_vertical_change(value):
    vertical_label.config(text=f"Vertical Value: {value}")



# Create the main window
root = Tk()
root.title("Himel's Sliders")

'''
The orient parameter in the Scale widget of Tkinter determines the orientation of the slider. 
It specifies whether the slider should be horizontal (HORIZONTAL) or vertical (VERTICAL).

orient=HORIZONTAL: Creates a horizontal slider.
orient=VERTICAL: Creates a vertical slider.
'''

# Horizontal Slider
horizontal_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=on_horizontal_change)
horizontal_slider.pack(pady=10)

horizontal_label = Label(root, text="Horizontal Value: 0")
horizontal_label.pack(pady=10)



# Vertical Slider
vertical_slider = Scale(root, from_=200, to=0, orient=VERTICAL, command=on_vertical_change)
vertical_slider.pack(pady=10)

vertical_label = Label(root, text="Vertical Value: 0")
vertical_label.pack(pady=10)


root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU
