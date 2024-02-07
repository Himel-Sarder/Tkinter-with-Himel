from tkinter import Tk, Scale, Label

def on_slider_change(value):
    label.config(text=f"Current Value: {value}")

root = Tk()
root.title("Slider with sliderlength Example")

# Slider with custom sliderlength
slider = Scale(root, from_=0, to=100, orient="horizontal", length=300, sliderlength=100, command=on_slider_change)
slider.pack(pady=20)

label = Label(root, text="Current Value: 0")
label.pack(pady=10)

root.mainloop()
